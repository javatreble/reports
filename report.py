import db_access
import db_utility


categories = ''
my_tuple_report=[]
my_tuple = db_access.get_all_areas()
template = "{:>3}  {:<25}  {:>10}  {:>25}     {:<30}"
line = template.format('ID', 'Name', "Num Loc", "Avg Value", 'Categories')
print(line)
for area_row in my_tuple:
    #print(area_row)
    categories = ''
    area_id = area_row[0]
    area_name = area_row[1]
    loc_num = db_utility.number_of_locations_by_area(area_id)
    avg_value = db_utility.get_average_measurements_for_area(area_id)
    if avg_value is None:
        avg_value = "        _________________"
    my_categories = db_access.get_categories_for_area(area_id)
    #print(my_categories)
    for category_row in my_categories:
        categories = categories + category_row + ', '
    if categories is None:
        pass
    else:
        categories = categories.rstrip(', ')
    template = "{:3}  {:25}  {:10}  {:25.4}     {:30}"
    line2 = template.format(area_id, area_name,loc_num,avg_value,categories)
    print(line2)
