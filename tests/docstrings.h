
#include <string>




namespace tudatpy {

static inline std::string get_docstring(std::string name, int variant=0) {

    if (name == "test") {
        return "test";

    } else {

#ifdef DEBUG
            return "No documentation found.";
#else
            throw std::runtime_error(
                    "Documentation was not found for:" + name + " (variant: " + std::to_string(variant) + ")");
#endif

    }

}
        

namespace interface {

static inline std::string get_docstring(std::string name, int variant=0) {

    if (name == "test") {
        return "test";

    } else {

#ifdef DEBUG
            return "No documentation found.";
#else
            throw std::runtime_error(
                    "Documentation was not found for:" + name + " (variant: " + std::to_string(variant) + ")");
#endif

    }

}
        

namespace spice {

static inline std::string get_docstring(std::string name, int variant=0) {

    if (name == "test") {
        return "test";

    } else if(name == "convert_julian_date_to_ephemeris_time") {
        return R"mydelimiter(Convert a Julian date to ephemeris time (equivalent to TDB in Spice).

            Extended Summary
            ----------------
            Function to convert a Julian date to ephemeris time, which is equivalent to barycentric
            dynamical time. A leap second kernel must have been loaded to use this function.

            Parameters
            ----------
            julian_date : int
                Julian date that is to be converted to ephemeris time.

            Returns
            -------
            ephemeris_time : float
                Julian date calculated from ephemeris time.


            )mydelimiter";

    } else if(name == "convert_ephemeris_time_to_julian_date") {
        return R"mydelimiter(Convert ephemeris time (equivalent to TDB) to a Julian date.

            Extended Summary
            ----------------
            Function to convert ephemeris time, which is nearly equal to barycentric dynamical time, to the
            Julian date. A leap second kernel must have been loaded to use this function.

            Parameters
            ----------
            ephemeris_time : float
                Ephemeris time that is to be converted to Julian date.

            Returns
            -------
            julian_date : float
                Julian date calculated from ephemeris time.


            )mydelimiter";

    } else if(name == "convert_date_string_to_ephemeris_time") {
        return R"mydelimiter(Converts a date string to ephemeris time.

            Extended Summary
            ----------------
            Function to convert a date string, for instance 1988 June 13, 3:29:48 to ephemeris time,
            wrapper for str2et_c spice function.

            Parameters
            ----------
            date_string : str
                String representing the date. See documentation of spice function str2et_c for details on supported formats.


            Returns
            -------
            ephemeris_time : str
                Ephemeris time corresponding to given date_string.


            )mydelimiter";

    } else if(name == "get_body_cartesian_state_at_epoch") {
        return R"mydelimiter(Get Cartesian state of a body, as observed from another body.

            Extended Summary
            ----------------
            This function returns the state of a body, relative to another body, in a frame specified
            by the user. Corrections for light-time correction and stellar
            aberration can be applied to obtain the state of one of the bodies, as observed from the other.
            Wrapper for spkezr_c spice function.

            Parameters
            ----------
            target_body_name : str
                Name of the body of which the state is to be obtained. A kernel with the
                ephemeris of this body must have been loaded. The string must be a spice-recognized
                name or ID.

            observer_body_name : str
                Name of the body relative to which the state is to be obtained.
                A kernel with theephemeris of this body must have been loaded.  The string must be a
                spice-recognized name or ID.

            reference_frame_name : str
                The spize-revognized name of the reference frame in which the state
                is to be returned. Spice kernel(s) required to perform the neccesary conversion from
                the states of the target and observer bodies to this frame need to have been loaded.

            aberration_corrections : str
                Setting for correction for setting corrections. See Spice
                documentation for extended discussion. Short summary: NONE: none, LT: light time
                corrected (one iteration for calculation), CN: light time corrected
                (multiple iterations, max 3) for calculation, S: Stellar aberration corrected. XLT and
                XCN can be provided to make the ephemerisTime input argument the transmission time,
                instead of receptionTime. Arguments can be combined (i.e."LT+S" or "XCN+S").

            ephemeris_time : float
                Observation time (or transmission time of observed light, see description
                of aberrationCorrections).


            Returns
            -------
            cartesian_state_vector : np.ndarray[6,]
                Cartesian state vector (x,y,z, position+velocity).


            )mydelimiter";

    } else if(name == "get_body_cartesian_position_at_epoch") {
        return R"mydelimiter(Get Cartesian position of a body, as observed from another body.

            Extended Summary
            ----------------
            This function returns the position of a body, relative to another body, in a frame specified
            by the user. Corrections for light-time correction and stellar
            aberration can be applied to obtain the state of one of the bodies, as observed from the other.
            Wrapper for spkpos_c spice function.

            Parameters
            ----------
            target_body_name : str
                Name of the body of which the state is to be obtained. A kernel with the
                ephemeris of this body must have been loaded. The string must be a spice-recognized
                name or ID.

            observer_body_name : str
                Name of the body relative to which the state is to be obtained.
                A kernel with theephemeris of this body must have been loaded.  The string must be a
                spice-recognized name or ID.

            reference_frame_name : str
                The spize-revognized name of the reference frame in which the state
                is to be returned. Spice kernel(s) required to perform the neccesary conversion from
                the states of the target and observer bodies to this frame need to have been loaded.

            aberration_corrections : str
                Setting for correction for setting corrections. See Spice
                documentation for extended discussion. Short summary: NONE: none, LT: light time
                corrected (one iteration for calculation), CN: light time corrected
                (multiple iterations, max 3) for calculation, S: Stellar aberration corrected. XLT and
                XCN can be provided to make the ephemerisTime input argument the transmission time,
                instead of receptionTime. Arguments can be combined (i.e."LT+S" or "XCN+S").

            ephemeris_time : float
                Observation time (or transmission time of observed light, see description
                of aberrationCorrections).



            )mydelimiter";

    } else if(name == "get_cartesian_state_from_tle_at_epoch") {
        return R"mydelimiter(Get Cartesian state of a satellite from its two-line element set at a specified epoch.

            Extended Summary
            ----------------
            This function retrieves the state of a satellite at a certain epoch by propagating the
            SGP or SDP models (near-Earth resp. deep space) with the given two-line elements (TLE).
            This function serves as a wrapper for the ev2lin_ function in CSpice.

            Parameters
            ----------
            epoch : float
                Time in seconds since J2000 at which the state is to be retrieved.
            tle : Tle
                Shared pointer to a Tle object containing the SGP/SDP model parameters as derived from the element set.

            Returns
            -------
            cartesian_state_vector : np.ndarray[6,]
                Cartesian state vector (x,y,z, position+velocity).


            )mydelimiter";

    } else if(name == "compute_rotation_quaternion_between_frames") {
        return R"mydelimiter(Compute quaternion of rotation between two frames.

            Extended Summary
            ----------------
            This function computes the quaternion of rotation between two frames at a given time instant.
            kernels defining the two frames, as well as any required intermediate frames, at the requested
            time must have been loaded. Wrapper for pxform_c spice function.

            Parameters
            ----------
            original_frame : 
                Reference frame from which the rotation is made.
            new_frame : 
                Reference frame to which the rotation is made.
            ephemeris_time : 
                Value of ephemeris time at which rotation is to be determined.

            Returns
            -------
             : 
                Rotation quaternion from original to new frame at given time.


            )mydelimiter";

    } else if(name == "compute_rotation_matrix_derivative_between_frames") {
        return R"mydelimiter(Computes time derivative of rotation matrix between two frames.

            Extended Summary
            ----------------
            This function computes the derivative of the rotation matrix between two frames at a given
            time instant. kernels defining the two frames, as well as any required intermediate frames, at
            the requested time must have been loaded. Wrapper for (part of) sxform_c spice function.

            Parameters
            ----------
            original_frame : 
                Reference frame from which the rotation is made.
            new_frame : 
                Reference frame to which the rotation is made.
            ephemeris_time : 
                Value of ephemeris time at which rotation is to be determined.

            Returns
            -------
             : 
                Time derivative of rotation matrix from original to new frame at given time.


            )mydelimiter";

    } else if(name == "get_angular_velocity_vector_of_frame_in_original_frame") {
        return R"mydelimiter(Computes the angular velocity of one frame w.r.t. to another frame.

            Extended Summary
            ----------------
            Computes the angular velocity of one frame w.r.t. to another frame. at a given
            time instant. kernels defining the two frames, as well as any required intermediate frames, at
            the requested time must have been loaded. Wrapper for xf2rav_c spice function (utilizing
            sxform_c).

            Parameters
            ----------
            original_frame : 
                Reference frame from which the rotation is made.
            new_frame : 
                Reference frame to which the rotation is made.
            ephemeris_time : 
                Value of ephemeris time at which rotation is to be determined.

            Returns
            -------
             : 
                Angular velocity of newFrame w.r.t. originalFrame, expressed in originalFrame.


            )mydelimiter";

    } else if(name == "get_body_properties") {
        return R"mydelimiter(Get property of a body from Spice.

            Extended Summary
            ----------------
            Function to retrieve a property of a body from Spice, wraps the bodvrd_c Spice function.

            Parameters
            ----------
            body_name : 
                Name of the body of which the property is to be retrieved.
            property : 
                Name of the property that is to be retrieved. Naming conventions can be found in the bodvrd_c function documentation.

            maximum_number_of_values : int
                Number of values by which the property is expressed (i.e. 1 for gravitational parameter, 3 for tri-axial ellipsoid principal axes).


            Returns
            -------
             : 
                Property value(s) expressed in an STL vector of doubles.


            )mydelimiter";

    } else if(name == "get_body_gravitational_parameter") {
        return R"mydelimiter(Get gravitational parameter of a body.

            Extended Summary
            ----------------
            This function retrieves the gravitational parameter of a body. Wraps the bodvrd_c spice function with "GM" as property type.

            Parameters
            ----------
            body : 
                Name of the body of which the parameter is to be retrieved.

            Returns
            -------
             : 
                Gravitational parameter of requested body.


            )mydelimiter";

    } else if(name == "get_average_radius") {
        return R"mydelimiter(Get the (arithmetic) mean of the three principal axes of the tri-axial ellipsoid shape.

            Extended Summary
            ----------------
            Returns the (arithmetic) mean of the three principal axes of the tri-axial ellipsoid shap of the requested body. Uses the bodvrd_c spice function with "RADII" as property type.

            Parameters
            ----------
            body : 
                Name of the body of which the average radius is to be retrieved.

            Returns
            -------
             : 
                Arithmetic mean of principal axes of tri-axial ellipsoid shape model of body.


            )mydelimiter";

    } else if(name == "convert_body_name_to_naif_id") {
        return R"mydelimiter(Convert a body name to its NAIF identification number.

            Extended Summary
            ----------------
            This function converts a body name to its NAIF identification number.The NAIF id number is
            required for a number of spice functions, whereas the name is easily interpretable by the user.
            Wrapper for the bods2c_c function.

            Parameters
            ----------
            body_name : 
                Name of the body for which NAIF id is to be retrieved.

            Returns
            -------
             : 
                NAIF id number for the body with bodyName.


            )mydelimiter";

    } else if(name == "check_body_property_in_kernel_pool") {
        return R"mydelimiter(Check if a certain property of a body is in the kernel pool.

            Extended Summary
            ----------------
            This function checks if a certain property of a body is in the kernel pool. These properties
            are defined in PCK kernels. Their names are given in the kernel file, typical names can be
            found in the Spice documentation. Wrapper for the bodfnd_c function.

            Parameters
            ----------
            body_name : 
                Name of the body of which the property is to be checked.
            body_property : 
                Name of the property of which the presence is to be checked, not case-sensitive.

            Returns
            -------
             : bool
                True if property is in pool, false if not.


            )mydelimiter";

    } else if(name == "get_standard_kernels") {
        return R"mydelimiter(Get the paths to the default legacy kernels.


            )mydelimiter";

    } else if(name == "load_standard_kernels") {
        return R"mydelimiter(Load the default legacy kernels.

            Parameters
            ----------
            kernel_paths : str
                Optional addition kernels to be loaded.


            )mydelimiter";

    } else if(name == "get_total_count_of_kernels_loaded") {
        return R"mydelimiter(Get the number of spice kernels currently loaded.

            Extended Summary
            ----------------
            This function returns the amount of Spice kernels that are loaded into the kernel pool. The
            same kernel can be loaded multple times. Wrapper for the ktotal_c function.

            Returns
            -------
            n_kernels : int
                Number of spice kernels currently loaded.


            )mydelimiter";

    } else if(name == "load_kernel") {
        return R"mydelimiter(Loads a Spice kernel into the pool.

            Extended Summary
            ----------------
            This function loads a Spice kernel into the kernel pool, from which it can be used by the
            various internal spice routines. Matters regarding the manner in which Spice handles different
            kernels containing the same information can be found in the spice required reading
            documentation, kernel section. Wrapper for the furnsh_c function.

            Parameters
            ----------
            file_path : str
                Path to the spice kernel to be loaded.


            )mydelimiter";

    } else if(name == "clear_kernels") {
        return R"mydelimiter(Clear all loaded spice kernels.

            Extended Summary
            ----------------
            This function removes all Spice kernels from the kernel pool. Wrapper for the kclear_c function.

            Returns
            -------
             : None
                
             : void
                


            )mydelimiter";

    } else {

#ifdef DEBUG
            return "No documentation found.";
#else
            throw std::runtime_error(
                    "Documentation was not found for:" + name + " (variant: " + std::to_string(variant) + ")");
#endif

    }

}

}

}

}