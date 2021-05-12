/*    Copyright (c) 2010-2019, Delft University of Technology
 *    All rigths reserved
 *
 *    This file is part of the Tudat. Redistribution and use in source and
 *    binary forms, with or without modification, are permitted exclusively
 *    under the terms of the Modified BSD license. You should have received
 *    a copy of the license with this file. If not, please or visit:
 *    http://tudat.tudelft.nl/LICENSE.
 *
 *    Notes
 *      In order to use the Spice interface, the C-Spice toolkit must be installed on your machine.
 *      It can be downloaded from http://naif.jpl.nasa.gov/naif/toolkit_C.html for all common
 *      operating systems. By placing the cspice folder in the external directory, or 1, 2 or 3
 *      folder levels above the project source directory, it will be automatically located by the
 *      cmake list. In order to use Spice with Tudat, please run the makeall file provided with
 *      Spice to compile the static library.
 *      IMPORTANT: Before being able to use it, the cspice.a file in the cspice/lib folder needs to
 *      be renamed to libcspice.a.
 *
 *      In addition, the USE_CSPICE variable needs to be set to 1 in the top-level CMakeLists.txt.
 *
 */

#ifndef TUDAT_SPICE_INTERFACE_H
#define TUDAT_SPICE_INTERFACE_H

#include <string>
#include <vector>

#include <Eigen/Core>
#include <Eigen/Geometry>

#include "tudat/basics/basicTypedefs.h"
#include "tudat/io/basicInputOutput.h"

extern "C" {
#include <cspice/SpiceUsr.h>
#include <cspice/SpiceZfc.h>
}

#include "tudat/astro/ephemerides/tleEphemeris.h"

namespace tudat {

namespace spice_interface {

/// Convert a Julian date to ephemeris time (equivalent to TDB in Spice).
/**
 * test
 * The following math is for documentation demonstration purposes
 * 
 * .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}
 * 
 * Function to convert a Julian date to ephemeris time, which is
 * equivalent to barycentric dynamical time. A leap second kernel
 * must have been loaded to use this function.
 *
 * @param julian_date
 *        Julian date that is to be converted to ephemeris time. * @return ephemeris_time 
 */
[[deprecated]]
double convertJulianDateToEphemerisTime(const double julianDate);

/// Convert ephemeris time (equivalent to TDB) to a Julian date.
/**
 * Function to convert ephemeris time, which is nearly equal to
 * barycentric dynamical time, to the Julian date. A leap second
 * kernel must have been loaded to use this function.
 *
 * @param ephemeris_time
 *        Ephemeris time that is to be converted to Julian date. * @return julian_date 
 */
double convertEphemerisTimeToJulianDate(const double ephemerisTime);

/// Converts a date string to ephemeris time.
/**
 * Function to convert a date string, for instance
 * 1988 June 13, 3:29:48 to ephemeris time, wrapper for `str2et_c`
 * spice function.
 *
 * @param date_string
 *        String representing the date. See documentation of spice
 *        function `str2et_c` for details on supported formats.
 * @return ephemeris_time 
 */
double convertDateStringToEphemerisTime(const std::string &dateString);

/// Get Cartesian state of a body, as observed from another body.
/**
 * This function returns the state of a body, relative to another
 * body, in a frame specified by the user. Corrections for light-time
 * correction and stellar aberration can be applied to obtain the
 * state of one of the bodies, as observed from the other. Wrapper
 * for `spkezr_c` spice function.
 *
 * @param target_body_name
 *        Name of the body of which the state is to be obtained. A kernel
 *        with the ephemeris of this body must have been loaded. The
 *        string must be a spice-recognized name or ID.
 * @param observer_body_name
 *        Name of the body relative to which the state is to be obtained.
 *        A kernel with the ephemeris of this body must have been loaded.
 *        The string must be a spice-recognized name or ID.
 * @param reference_frame_name
 *        The spice-recognized name of the reference frame in which the
 *        state is to be returned. Spice kernel(s) required to perform
 *        the necessary conversion from the states of the target and
 *        observer bodies to this frame need to have been loaded.
 * @param aberration_corrections
 *        Setting for correction for setting corrections. See Spice
 *        documentation for extended discussion.
 *        Short summary:
 *        
 *        - NONE: none
 *        - LT: light time corrected (one iteration for calculation)
 *        - CN: light time corrected (multiple iterations, max 3)
 *          for calculation,
 *        - S: Stellar aberration corrected.
 *        - XLT and XCN can be provided to make the ephemeris time
 *          input argument the transmission time,
 *          instead of reception time.
 *        
 *        Arguments can be combined (i.e."LT+S" or "XCN+S").
 * @param ephemeris_time
 *        Observation time (or transmission time of observed light, see description
 *        of aberrationCorrections).
 * @return cartesian_state_vector 
 */
Eigen::Vector6d getBodyCartesianStateAtEpoch(
    const std::string &targetBodyName, const std::string &observerBodyName,
    const std::string &referenceFrameName, const std::string &aberrationCorrections,
    const double ephemerisTime);

/// Get Cartesian position of a body, as observed from another body.
/**
 * This function returns the position of a body, relative to another
 * body, in a frame specified by the user. Corrections for light-time
 * correction and stellar aberration can be applied to obtain the
 * state of one of the bodies, as observed from the other. Wrapper
 * for `spkpos_c` spice function.
 *
 * @param target_body_name
 *        Name of the body of which the state is to be obtained. A kernel
 *        with the ephemeris of this body must have been loaded. The
 *        string must be a spice-recognized name or ID.
 * @param observer_body_name
 *        Name of the body relative to which the state is to be obtained.
 *        A kernel with the ephemeris of this body must have been loaded.
 *        The string must be a spice-recognized name or ID.
 * @param reference_frame_name
 *        The spice-recognized name of the reference frame in which the
 *        state is to be returned. Spice kernel(s) required to perform
 *        the necessary conversion from the states of the target and
 *        observer bodies to this frame need to have been loaded.
 * @param aberration_corrections
 *        Setting for correction for setting corrections. See Spice
 *        documentation for extended discussion.
 *        Short summary:
 *        
 *        - NONE: none
 *        - LT: light time corrected (one iteration for calculation)
 *        - CN: light time corrected (multiple iterations, max 3)
 *          for calculation,
 *        - S: Stellar aberration corrected.
 *        - XLT and XCN can be provided to make the ephemeris time
 *          input argument the transmission time,
 *          instead of reception time.
 *        
 *        Arguments can be combined (i.e."LT+S" or "XCN+S").
 * @param ephemeris_time
 *        Observation time (or transmission time of observed light, see description
 *        of aberrationCorrections).
 */
Eigen::Vector3d getBodyCartesianPositionAtEpoch(const std::string &targetBodyName,
                                                const std::string &observerBodyName,
                                                const std::string &referenceFrameName,
                                                const std::string &aberrationCorrections,
                                                const double ephemerisTime);

/// Get Cartesian state of a satellite from its two-line element set at a specified epoch.
/**
 * This function retrieves the state of a satellite at a certain epoch
 * by propagating the SGP or SDP models (near-Earth resp. deep space)
 * with the given two-line elements (TLE). This function serves as a
 * wrapper for the `ev2lin_` function in CSpice.
 *
 * @param epoch
 *        Time in seconds since J2000 at which the state is to be retrieved. * @param tle
 *        Shared pointer to a Tle object containing the SGP/SDP model parameters as derived from the element set. * @return cartesian_state_vector 
 */
Eigen::Vector6d getCartesianStateFromTleAtEpoch(double epoch, std::shared_ptr<ephemerides::Tle> tle);

/// Compute quaternion of rotation between two frames.
/**
 * This function computes the quaternion of rotation between two
 * frames at a given time instant. kernels defining the two frames,
 * as well as any required intermediate frames, at the requested
 * time must have been loaded. Wrapper for `pxform_c` spice function.
 *
 * @param original_frame
 *        Reference frame from which the rotation is made. * @param new_frame
 *        Reference frame to which the rotation is made. * @param ephemeris_time
 *        Value of ephemeris time at which rotation is to be determined. * @return  
 */
Eigen::Quaterniond computeRotationQuaternionBetweenFrames(const std::string &originalFrame,
                                                          const std::string &newFrame,
                                                          const double ephemerisTime);

Eigen::Matrix3d computeRotationMatrixBetweenFrames(const std::string &originalFrame,
                                                   const std::string &newFrame,
                                                   const double ephemerisTime);

/// Computes time derivative of rotation matrix between two frames.
/**
 * This function computes the derivative of the rotation matrix
 * between two frames at a given time instant. kernels defining the
 * two frames, as well as any required intermediate frames, at the
 * requested time must have been loaded. Wrapper for (part of)
 * `sxform_c` spice function.
 *
 * @param original_frame
 *        Reference frame from which the rotation is made. * @param new_frame
 *        Reference frame to which the rotation is made. * @param ephemeris_time
 *        Value of ephemeris time at which rotation is to be determined. * @return  
 */
Eigen::Matrix3d computeRotationMatrixDerivativeBetweenFrames(const std::string &originalFrame,
                                                             const std::string &newFrame,
                                                             const double ephemerisTime);

/// Computes the angular velocity of one frame w.r.t. to another frame.
/**
 * Computes the angular velocity of one frame w.r.t. to another frame.
 * at a given time instant. kernels defining the two frames, as well
 * as any required intermediate frames, at the requested time must
 * have been loaded. Wrapper for `xf2rav_c`_ spice function (utilizing
 * `sxform_c`_).
 * 
 * .. _`xf2rav_c`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/xf2rav_c.html
 * .. _`sxform_c`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/sxform_c.html
 *
 * @param original_frame
 *        Reference frame from which the rotation is made. * @param new_frame
 *        Reference frame to which the rotation is made. * @param ephemeris_time
 *        Value of ephemeris time at which rotation is to be determined. * @return  
 */
Eigen::Vector3d getAngularVelocityVectorOfFrameInOriginalFrame(const std::string &originalFrame,
                                                               const std::string &newFrame,
                                                               const double ephemerisTime);

std::pair<Eigen::Quaterniond, Eigen::Matrix3d> computeRotationQuaternionAndRotationMatrixDerivativeBetweenFrames(
    const std::string &originalFrame, const std::string &newFrame, const double ephemerisTime);

/// Get property of a body from Spice.
/**
 * Function to retrieve a property of a body from Spice, wraps the bodvrd_c Spice function.
 *
 * @param body_name
 *        Name of the body of which the property is to be retrieved. * @param property
 *        Name of the property that is to be retrieved. Naming conventions can be found
 *        in the `bodvrd_c`_ function documentation.
 *        
 *        .. _`bodvrd_c`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/bodvrd_c.html
 * @param maximum_number_of_values
 *        Number of values by which the property is expressed (i.e. 1 for
 *        gravitational parameter, 3 for tri-axial ellipsoid principal axes).
 * @return  
 */
std::vector<double> getBodyProperties(const std::string &body,
                                      const std::string &property,
                                      const int maximumNumberOfValues = 1);

/// Get gravitational parameter of a body.
/**
 * This function retrieves the gravitational parameter of a body.
 * Wraps the `bodvrd_c`_ spice function with "GM" as property type.
 * 
 * .. _`bodvrd_c`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/bodvrd_c.html
 *
 * @param body
 *        Name of the body of which the parameter is to be retrieved. * @return  
 */
double getBodyGravitationalParameter(const std::string &body);

/// Get the (arithmetic) mean of the three principal axes of the tri-axial ellipsoid shape.
/**
 * Returns the (arithmetic) mean of the three principal axes of the
 * tri-axial ellipsoid shape of the requested body. Uses the
 * `bodvrd_c` spice function with "RADII" as property type.
 * 
 * .. _`bodvrd_c`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/bodvrd_c.html
 *
 * @param body
 *        Name of the body of which the average radius is to be retrieved. * @return  
 */
double getAverageRadius(const std::string &body);

/// Convert a body name to its NAIF identification number.
/**
 * This function converts a body name to its NAIF identification
 * number. The NAIF id number is required for a number of spice
 * functions, whereas the name is easily interpretable by the user.
 * Wrapper for the ``bods2c_c`` function.
 *
 * @param body_name
 *        Name of the body for which NAIF id is to be retrieved. * @return  
 */
int convertBodyNameToNaifId(const std::string &bodyName);

/// Check if a certain property of a body is in the kernel pool.
/**
 * This function checks if a certain property of a body is in the
 * kernel pool. These properties are defined in PCK kernels. Their
 * names are given in the kernel file, typical names can be found in
 * the Spice documentation. Wrapper for the `bodfnd_c`_ function.
 * 
 * .. _`bodfnd_c`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/bodfnd_c.html
 *
 * @param body_name
 *        Name of the body of which the property is to be checked. * @param body_property
 *        Name of the property of which the presence is to be checked, not case-sensitive. * @return  
 */
bool checkBodyPropertyInKernelPool(const std::string &bodyName, const std::string &bodyProperty);

/// Loads a Spice kernel into the pool.
/**
 * This function loads a Spice kernel into the kernel pool, from which
 * it can be used by the various internal spice routines. Matters
 * regarding the manner in which Spice handles different kernels
 * containing the same information can be found in the spice required
 * reading documentation, kernel section. Wrapper for the `furnsh_c`_
 * function.
 * 
 * .. _`furnsh_c`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/furnsh_c.html
 *
 * @param file_path
 *        Path to the spice kernel to be loaded. */
void loadSpiceKernelInTudat(const std::string &fileName);

/// Get the number of spice kernels currently loaded.
/**
 * This function returns the amount of Spice kernels that are loaded
 * into the kernel pool. The same kernel can be loaded multiple times.
 * Wrapper for the `ktotal_c`_ function.
 * 
 * .. _`ktotal_c`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/ktotal_c.html
 * @return n_kernels 
 */
int getTotalCountOfKernelsLoaded();

/// Clear all loaded spice kernels.
/**
 * This function removes all Spice kernels from the kernel pool.
 * Wrapper for the `kclear_c`_ function.
 * 
 * .. _`kclear_c`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/kclear_c.html
 */
void clearSpiceKernels();

/// Get the paths to the default legacy kernels.
/**
 */
std::vector<std::string> getStandardSpiceKernels(const std::vector<std::string> alternativeEphemerisKernels =
                                                     std::vector<std::string>());

/// Load the default legacy kernels.
/**
 *
 * @param kernel_paths
 *        Optional addition kernels to be loaded. */
void loadStandardSpiceKernels(const std::vector<std::string> alternativeEphemerisKernels =
                                  std::vector<std::string>());

}// namespace spice_interface
}// namespace tudat

#endif// TUDAT_SPICE_INTERFACE_H
