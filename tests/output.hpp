
#include <string>




namespace tudatpy {

static inline std::string get_docstring(std::string name, int variant=0) {

    if (name == "test") {
        return "test";

    } else {
        return "else";
    }
}
        

namespace interface {

static inline std::string get_docstring(std::string name, int variant=0) {

    if (name == "test") {
        return "test";

    } else {
        return "else";
    }
}
        

namespace spice {

static inline std::string get_docstring(std::string name, int variant=0) {

    if (name == "test") {
        return "test";

    } else if(name == "convert_julian_date_to_ephemeris_time") {
        return convert_julian_date_to_ephemeris_time;

    } else if(name == "convert_ephemeris_time_to_julian_date") {
        return convert_ephemeris_time_to_julian_date;

    } else if(name == "convert_date_string_to_ephemeris_time") {
        return convert_date_string_to_ephemeris_time;

    } else if(name == "get_body_cartesian_state_at_epoch") {
        return get_body_cartesian_state_at_epoch;

    } else if(name == "get_body_cartesian_position_at_epoch") {
        return get_body_cartesian_position_at_epoch;

    } else if(name == "get_cartesian_state_from_tle_at_epoch") {
        return get_cartesian_state_from_tle_at_epoch;

    } else if(name == "compute_rotation_quaternion_between_frames") {
        return compute_rotation_quaternion_between_frames;

    } else if(name == "compute_rotation_matrix_deri_vative_between_frames") {
        return compute_rotation_matrix_deri_vative_between_frames;

    } else if(name == "get_angular_velocity_vector_of_frame_in_original_frame") {
        return get_angular_velocity_vector_of_frame_in_original_frame;

    } else if(name == "get_body_properties") {
        return get_body_properties;

    } else if(name == "get_body_gravitational_parameter") {
        return get_body_gravitational_parameter;

    } else if(name == "get_average_radius") {
        return get_average_radius;

    } else if(name == "convert_body_name_to_naif_id") {
        return convert_body_name_to_naif_id;

    } else if(name == "check_body_property_in_kernel_pool") {
        return check_body_property_in_kernel_pool;

    } else if(name == "get_standard_kernels") {
        return get_standard_kernels;

    } else if(name == "load_standard_kernels") {
        return load_standard_kernels;

    } else if(name == "get_total_count_of_kernels_loaded") {
        return get_total_count_of_kernels_loaded;

    } else if(name == "load_kernel") {
        return load_kernel;

    } else if(name == "clear_kernels") {
        return clear_kernels;

    } else {
        return "else";
    }
}

}

}

}