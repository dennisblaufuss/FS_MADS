# Dennis Blaufuss
# 8458109
# 21.10.21
# Option 2 - OCR boxes

"""
Plain English Explanition:
The Function first checks if the boxes are within in table. (regarding x and y coordinates)
All boxes that aren't are removed from the list.
Now the function computes the end of each box (for easier use afterwards).
After That all boxes are compared with each other and possible empty columns are looked for.
Those possible columns are added to a list. Those are saved as starting_x and ending_x.
Now for each possilbe column in the list it is checked if there is another box in that space.
If yes the possible column is removed.
Now one last check has to happen:
There could be columns overlapping. Thus we have to check if there is for any column a biger one spaning the same space (and more obviously)
If yes, this column is removed as well.
Now we should (hopefully :P) have our complete list of columns.
For each columns now the approximate mid has to be computed and added to the seperator list.
This seperator list now gets returned.
"""


class Table:

    def __init__(self, top_left_x, top_left_y, width, height):
        # Represents a table on a page through the top left corner and width and height, relative to the top left of the page.
        # You can assume that
        # * all numbers are positive (top_left_x or top_left_y can be 0)
        # * width is larger than 0
        # * height is larger than 0
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height

    def calculate_columns(self, ocr_boxes):
        # Returns a list of column separators relative to the top_left_x of the table without crossing OCR boxes.
        # Note that:
        # * OCR boxes are given as a list of lists (for example:  [[10, 10, 100, 5], [10, 20, 80, 5]])
        # * each box has a top_left_x, top_left_y, width and height (in that order) relative to the page (not table!)
        # * you can assume that the table itself is not crossing any OCR box;
        # * if there are no OCR boxes within the table borders return an empty list ([]).
        # * the algorithm must not create column that is totally empty (i.e has not OCR box in it);
        # * the column separator should be (approximately) in the middle of the empty space between OCR boxes.
        # YOUR CODE STARTS HERE
        for box in ocr_boxes:
            # removes all boxes that are out of the table
            # you would have to remove regarding y achsis as well -> had no time to implement
            if box[0] > (self.top_left_x + self.width) or box[1] < self.top_left_x:
                ocr_boxes.remove(box)

        if len(ocr_boxes) < 2:
            # returns empty list if there are either no or one box within in the table
            return []

        for box in ocr_boxes:
            # appends ending coordinate to boxes
            # doing this after kicking out irrelevant boxes and ending early (see if statement) prevents unnescesarry time
            box.append(box[0] + box[2])

        col_list = []

        for box in ocr_boxes:
            # it would save time to skip the comparing with itself
            temp = []
            for compare_box in ocr_boxes:
                # ERROR: IDK why but the code does not append to temp in here.
                # if i check manually it does tho
                # has to be some stupid error... fml
                if box[4] < compare_box[0]:
                    temp.append([box[4], compare_box[0]])
            for col in temp:
                # there should be a faster way of implementing -> checking directly for all boxes.
                # thus we wouldn't have to overwrite stuff over and over again.
                for compare_box in ocr_boxes:
                    if compare_box[0] > col[0] or compare_box[4] < col[1]:
                        temp.remove(col)
            col_list.append(temp)

        # check for overlapping columns
        for col in col_list:
            # there should be a faster way here aswell
            for compare_col in col_list:
                if compare_col[0] <= col[0] and compare_col[1] >= col[1] and compare_col[1] - compare_col[0] > col[1] - col[0]:
                    col_list.remove(col)

        sep_list = []
        for col in col_list:
            # has to be table coordinates and not global coordinates
            temp_sep = col[0] + ((col[1] - col[0])//2)
            sep = temp_sep - self.top_left_x
            sep_list.append(sep)
        # YOUR CODE ENDS HERE


t1 = Table(10, 10, 410, 210)
# I change the input here to a list and not two -> hope thats fine
c1 = t1.calculate_columns([[11, 11, 79, 29], [100, 11, 90, 29]])
# c1 should be [95]

t2 = Table(10, 10, 410, 210)
c2 = t2.calculate_columns([11, 11, 79, 29], [100, 11, 90, 29], [11, 51, 150, 29])
# c2 should be []
