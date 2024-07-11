
def deep_update(base_dict, update_with):
    # iterate over each item in the dict
    for key, value in update_with.items():

        # if value is a dict
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)

            # if original value is also a dict then run it through the same function
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)

            # if original value is NOT a dict then just set the new value
            else:
                base_dict[key] = value

        # If new value is NOT a dict
        else:
            base_dict[key] = value

    return base_dict
