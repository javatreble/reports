import db_access

def get_average_measurements_for_area(area_id):
    """
    Returns the average value of all measurements for all locations in the given area.
    Returns None if there are no measurements.
    """
    measurement_total = 0
    count = 0
    my_tuple = db_access.get_locations_for_area(area_id)

    #print(my_tuple)

    for row in my_tuple:
        my_tuple_loc = db_access.get_measurements_for_location(row[0])
        #print my_tuple_loc
        for row_loc in my_tuple_loc:
            count = count + 1;
            measurement_total = measurement_total + row_loc[1]

    if count==0:
        return None

    return measurement_total/count



def number_of_locations_by_area(area_id):
    """
    Returns the number of locations for the given area.
    """

    my_tuple = db_access.get_locations_for_area(area_id)

    #print(len(my_tuple))

    return len(my_tuple)

