
def main():
    box_size = int(raw_input("How big is the square? "))

    def draw_a_box():

    y = 0
    while y < box_size:
        x = 0
        row = ""
        y = y + 1   
        while x < box_size:
            x = x + 1
            row = row + " *"
        print row
main()