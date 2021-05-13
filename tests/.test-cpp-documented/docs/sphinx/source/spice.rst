``test-cpp::interface::spice``
==============================
This module provides an interface to the Spice package.

Test notes!





Functions
---------

.. doxygenfunction:: test-cpp::interface::spice::convertjuliandatetoephemeristime

.. doxygenfunction:: test-cpp::interface::spice::convertEphemerisTimeToJulianDate

.. doxygenfunction:: test-cpp::interface::spice::convertDateStringToEphemerisTime

.. doxygenfunction:: test-cpp::interface::spice::getBodyCartesianStateAtEpoch

.. doxygenfunction:: test-cpp::interface::spice::getBodyCartesianPositionAtEpoch

.. doxygenfunction:: test-cpp::interface::spice::getCartesianStateFromTleAtEpoch

.. doxygenfunction:: test-cpp::interface::spice::computeRotationQuaternionBetweenFrames

.. doxygenfunction:: test-cpp::interface::spice::computeRotationMatrixDerivativeBetweenFrames

.. doxygenfunction:: test-cpp::interface::spice::getAngularVelocityVectorOfFrameInOriginalFrame

.. doxygenfunction:: test-cpp::interface::spice::getBodyProperties

.. doxygenfunction:: test-cpp::interface::spice::getBodyGravitationalParameter

.. doxygenfunction:: test-cpp::interface::spice::getAverageRadius

.. doxygenfunction:: test-cpp::interface::spice::convertBodyNameToNaifId

.. doxygenfunction:: test-cpp::interface::spice::checkBodyPropertyInKernelPool

.. doxygenfunction:: test-cpp::interface::spice::getStandardKernels

.. doxygenfunction:: test-cpp::interface::spice::loadStandardKernels

.. doxygenfunction:: test-cpp::interface::spice::getTotalCountOfKernelsLoaded

.. doxygenfunction:: test-cpp::interface::spice::loadKernel

.. doxygenfunction:: test-cpp::interface::spice::clearKernels




Classes
-------

.. doxygenclass:: test-cpp::interface::spice::SpiceEphemeris
    :members:



