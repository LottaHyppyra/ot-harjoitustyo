from entities.constants import FLOOR, PLAYER, FINISH, SMUDGE_STICK

class Player():
    def __init__(self, labyrint, inventory=1):
        self.labyrint = labyrint
        self.inventory = inventory

    def get_coords(self):
        for y_coord in range(len(self.labyrint)):
            for x_coord in range(len(self.labyrint[y_coord])):
                if self.labyrint[y_coord][x_coord] == PLAYER:
                    return (x_coord, y_coord)
        return None

    def move(self, x_diff, y_diff):
        pos_now = self.get_coords()

        if self.labyrint[pos_now[1] + y_diff][pos_now[0] + x_diff] == FLOOR:
            self.labyrint[pos_now[1]][pos_now[0]] = FLOOR
            self.labyrint[pos_now[1] + y_diff][pos_now[0] + x_diff] = PLAYER
            return False

        if self.labyrint[pos_now[1] + y_diff][pos_now[0] + x_diff] == FINISH:
            self.labyrint[pos_now[1]][pos_now[0]] = FLOOR
            return True

        if self.labyrint[pos_now[1] + y_diff][pos_now[0] + x_diff] == SMUDGE_STICK:
            self.inventory += 1
            self.labyrint[pos_now[1]][pos_now[0]] = FLOOR
            self.labyrint[pos_now[1] + y_diff][pos_now[0] + x_diff] = PLAYER
            return False

        return False

    def use_smudge(self):
        if self.inventory == 0:
            return False

        self.inventory -= 1
        return True

    def count_smudges(self):
        return self.inventory
