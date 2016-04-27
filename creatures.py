
#
# @file     creatures.py
# @author   Eshan Shafeeq
# @version  0.5
# @date     27 August 2015
# @brief    This file contains the pixels for the creatures that can be
#           deployed while running the game. If you want to save your own creature.
#           make your creature on the game. And use the save feature to save the creature
#           date to a file. Which will be a list of coordinates like these.
#


class creatures():
    """docstring for creatures"""
    def __init__(self):
        pass

    def get_creature(self, cid):
        if cid == 0:
            return [[1,5],[2,5],[1,6],[2,6],[11,5],[11,6],[11,7],[12,4],[12,8],[13,3],[13,9],[14,3],[14,9],[15,6],[16,4],[16,8],[17,5],[17,7],[17,6],[18,6],[21,3],[21,4],[21,5],[22,3],[22,4],[22,5],[23,2],[23,6],[25,2],[25,6],[25,7],[25,1],[35,3],[35,4],[36,3],[36,4]]
        if cid == 1:
            return [[2, 4],[2, 5],[2, 6],[2, 10],[2, 11],[2, 12],[4, 2],[4, 7],[4, 9],[4, 14],[5, 2],[5, 7],[5, 9],[5, 14],[6, 2],[6, 7],[6, 9],[6, 14],[7, 4],[7, 5],[7, 6],[7, 10],[7, 11],[7, 12],[9, 4],[9, 5],[9, 6],[9, 10],[9, 11],[9, 12],[10, 2],[10, 7],[10, 9],[10, 14],[11, 2],[11, 7],[11, 9],[11, 14],[12, 2],[12, 7],[12, 9],[12, 14],[14, 4],[14, 5],[14, 6],[14, 10],[14, 11],[14, 12]]
        if cid == 2:
            return [[1, 1],[2, 1],[3, 1],[4, 1],[5, 1],[6, 1],[7, 1],[8, 1],[10, 1],[11, 1],[12, 1],[13, 1],[14, 1],[18, 1],[19, 1],[20, 1],[27, 1],[28, 1],[29, 1],[30, 1],[31, 1],[32, 1],[33, 1],[35, 1],[36, 1],[37, 1],[38, 1],[39, 1]]
