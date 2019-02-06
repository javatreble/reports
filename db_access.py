
import sqlite3

from os.path import split, join



def get_all_areas():
    """
    Returns a list of tuples representing all the rows in the
    area table.
    """
    this_dir = split(__file__)[0]
    fname = join(this_dir, 'measures.sqlite')
    conn = sqlite3.connect(fname)
    my_tuple = ()


    try:
        crs = conn.cursor()
        cmd1 = "select * from area"
        crs.execute(cmd1)
        my_tuple =  crs.fetchall()
        #print(my_tuple)
        return my_tuple

    finally:
        conn.close()


def get_locations_for_area(area_id):
    """
    Return a list of tuples giving the locations for the given area.
    """

    this_dir = split(__file__)[0]
    fname = join(this_dir, 'measures.sqlite')
    conn = sqlite3.connect(fname)
    my_tuple = ()

    try:
        crs = conn.cursor()
        cmd1 = "select * from  location where location_area = ?"
        crs.execute(cmd1, [area_id])
        my_tuple = crs.fetchall()
        #print(my_tuple)

        for row in my_tuple:
            #print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
            #print row[1]

            loc = row[1]
            #print loc

        return my_tuple

    finally:
        conn.close()

def get_measurements_for_location(location_id):
    """
    Return a list of tuples giving the measurement rows for the given location.
    """
    this_dir = split(__file__)[0]
    fname = join(this_dir, 'measures.sqlite')
    conn = sqlite3.connect(fname)
    my_tuple = ()

    try:
        crs = conn.cursor()
        cmd1 = "select * from  measurement where measurement_location = ?"
        crs.execute(cmd1, [location_id])
        my_tuple = crs.fetchall()
        #print(my_tuple)

        return my_tuple

    finally:
        conn.close()


def get_categories_for_area(area_id):
    """
    Return a list of rows from the category table that all contain the given area.
    """
    this_dir = split(__file__)[0]
    fname = join(this_dir, 'measures.sqlite')
    conn = sqlite3.connect(fname)
    my_tuple = []
    my_tuple2 = []
    categories = []
    try:
        crs = conn.cursor()
        cmd1 = "select * from  category_area where area_id = ?"
        crs.execute(cmd1, [area_id])
        my_tuple = crs.fetchall()
        #print(my_tuple)

        for row in my_tuple:
            crs2 = conn.cursor()
            #print row[0]
            cmd2 = "select * from  category where category_id = ?"
            crs2.execute(cmd2, [row[0]])
            my_tuple2 = crs2.fetchall()
            for category_row in my_tuple2:
                categories.append(category_row[1])

        #print (categories)
        return categories

    finally:
        conn.close()
        conn.close()