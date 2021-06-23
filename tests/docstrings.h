
#include <string>




namespace  {

static inline std::string get_docstring(std::string name, int variant=0) {

    if (name == "test") {
        return "test";

    } else {
        return "No documentation found.";
    }

}

}