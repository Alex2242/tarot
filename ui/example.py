# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 08:54:32 2019

@author: codel
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import random

WINDOW_SIZE = 1500, 1000

ratio = 304/748
card_width = 100
card_length = card_width*ratio
CARD_RECT_PAIR = QRect(0, 0, card_width, card_length)
CARD_RECT_ODD = QRect(0, 0, card_length, card_width)
CARD_SPACING_X = 110
CARD_BACK = QImage(os.path.join('images', 'dos.png'))

DEAL_RECT = QRect(30, 30, card_width, card_length)

OFFSET_X = 50
OFFSET_Y = 50
CENTER_X = WINDOW_SIZE[0]//2-card_width/2
CENTER_Y = WINDOW_SIZE[1]//3-card_width/2
SPACE_X = 200  
SPACE_Y = 200  
WORK_STACK_X = [CENTER_X, CENTER_X-SPACE_X-card_width/2, CENTER_X, CENTER_X+
                SPACE_X+card_width/2]
WORK_STACK_Y = [CENTER_Y+SPACE_Y, CENTER_Y, CENTER_Y-SPACE_Y-card_length, 
                CENTER_Y]


SIDE_FACE = 0
SIDE_BACK = 1

BOUNCE_ENERGY = 0.8

# We store cards as numbers 1-13, since we only need
# to know their order for solitaire.
#SUITS = ["C", "S", "H", "D"]


class Signals(QObject):
    """
    PyQt signals class
    """
    # The following elements are attributes
    complete = pyqtSignal() #
    clicked = pyqtSignal()
    doubleclicked = pyqtSignal()


class Card(QGraphicsPixmapItem):
    """
    Graphic widget inherited class aimed at modelling the card
    """
    #def __init__(self, value, suit, *args, **kwargs):
    def __init__(self, value, position, scene,*args, **kwargs):
        super(Card, self).__init__(*args, **kwargs)

        self.signals = Signals() #Interaction with user

        self.stack = None  # Stack this card currently is in.
        self.child = None  # Card stacked on this one (for work deck).

        # Store the value (& suit) of the cards internal to it.
        self.value = value
        #self.suit = suit
        self.side = None # Face or back
        
        # For end animation only.
        self.vector = None

        # Cards have no internal transparent areas, so we can use this faster method.
        self.setShapeMode(QGraphicsPixmapItem.BoundingRectShape)
        self.setFlag(QGraphicsPixmapItem.ItemIsMovable)
        self.setFlag(QGraphicsPixmapItem.ItemSendsGeometryChanges)
        self.setPos(position[0],position[1])
        
        self.load_images(scene)
        scene.addItem(self)
        
        
    
    def load_images(self,scene):
        self.image_face = QPixmap(
            #os.path.join('cards', '%s%s.png' % (self.value,self.suit))
        os.path.join('images', '%s.png' % (self.value)))
        self.image_face = (self.image_face).scaledToWidth(card_width) 
        
        self.face = self.image_face
        self.setPixmap(self.face)
        

    def mousePressEvent(self, e):
        if not self.is_face_up and self.stack.cards[-1] == self:
            self.turn_face_up()  # We can do this without checking.
            e.accept()
            return

        if self.stack and not self.stack.is_free_card(self):
            e.ignore()
            return

        self.stack.activate()

        e.accept()

        super(Card, self).mouseReleaseEvent(e)

    def mouseReleaseEvent(self, e):
        self.stack.deactivate()

        items = self.collidingItems()
        if items:
            # Find the topmost item from a different stack:
            for item in items:
                if ((isinstance(item, Card) and item.stack != self.stack) or
                    (isinstance(item, StackBase) and item != self.stack)):

                    if item.stack.is_valid_drop(self):
                        # Remove card + all children from previous stack, add to the new.
                        # Note: the only place there will be children is on a workstack.
                        cards = self.stack.remove_card(self)
                        item.stack.add_cards(cards)
                        break

        # Refresh this card's stack, pulling it back if it was dropped.
        self.stack.update()

        super(Card, self).mouseReleaseEvent(e)

    def mouseDoubleClickEvent(self, e):
        if self.stack.is_free_card(self):
            self.signals.doubleclicked.emit()
            e.accept()

        super(Card, self).mouseDoubleClickEvent(e)



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(QRectF(0, 0, *WINDOW_SIZE))

        felt = QBrush((QPixmap(os.path.join('images','background.jpg'))).scaledToWidth(WINDOW_SIZE[0]))
        self.scene.setBackgroundBrush(felt)

        view.setScene(self.scene)

        self.ScoreJ1 = QLCDNumber()
        self.ScoreJ1.setGeometry(CENTER_X+250,525, 400, 600)           #(CENTER_X+120, CENTER_Y+300, 100, 50)
        self.ScoreJ1.setObjectName("ScoreJ1")
        self.ScoreJ1.setStyleSheet("color: black;")
        self.ScoreJ1.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.ScoreJ1)

        self.ScoreJ2 = QLCDNumber()
        self.ScoreJ2.setGeometry(CENTER_X-525, CENTER_Y, 200, 200)
        self.ScoreJ2.setObjectName("ScoreJ2")
        self.ScoreJ2.setStyleSheet("color: white;")
        self.ScoreJ2.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.ScoreJ2)
 
        self.ScoreJ3 = QLCDNumber()
        self.ScoreJ3.setGeometry(WORK_STACK_X[0]-275, 50, 200, 200)
        self.ScoreJ3.setObjectName("ScoreJ3")
        self.ScoreJ3.setStyleSheet("color: white;")
        self.ScoreJ3.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.ScoreJ3)

        self.ScoreJ4 = QLCDNumber()
        self.ScoreJ4.setGeometry(CENTER_X+275, CENTER_Y, 200, 200)
        self.ScoreJ4.setObjectName("ScoreJ4")
        self.ScoreJ4.setStyleSheet("color: white;")
        self.ScoreJ4.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.ScoreJ4)
    

        self.BetFiller = QSpinBox()
        self.BetFiller.setGeometry(150, 780, 100, 70)
        font = QFont()
        font.setPointSize(20)
        self.BetFiller.setFont(font)
        self.BetFiller.setObjectName("BetFiller")
        self.scene.addWidget(self.BetFiller)
        
        self.cardJ1 = Card(1,(WORK_STACK_X[0], WORK_STACK_Y[0]),self.scene)
        
        self.cardJ2 = Card(2,(WORK_STACK_X[1], WORK_STACK_Y[1]),self.scene)
        
        self.cardJ3 = Card(3,(WORK_STACK_X[2], WORK_STACK_Y[2]),self.scene)

        self.cardJ4 = Card(4,(WORK_STACK_X[3], WORK_STACK_Y[3]),self.scene)
        
        self.cardJ1_choice1 = Card(5,(CENTER_X-350,750-card_length//2),
                                  self.scene)
        
        self.cardJ1_choice2 = Card(6,(CENTER_X-175,750-card_length//2),
                                  self.scene)
        
        self.cardJ1_choice3 = Card(7,(WORK_STACK_X[0],750-card_length//2),
                                  self.scene)
        
        self.cardJ1_choice4 = Card(8,(CENTER_X+175,750-card_length//2),
                                  self.scene)
        
        self.cardJ1_choice5 = Card(9,(CENTER_X+350,750-card_length//2),
                                  self.scene)
        
        self.ScoresetJ1 = QLCDNumber()
        self.ScoresetJ1.setGeometry(CENTER_X-7, CENTER_Y+70+50, 70, 30)
        self.ScoresetJ1.setObjectName("ScoresetJ1")
        self.ScoresetJ1.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.ScoresetJ1)
        
        self.ScoresetJ3 = QLCDNumber()
        self.ScoresetJ3.setGeometry(CENTER_X+10, CENTER_Y+70-50, 51, 20)
        self.ScoresetJ3.setObjectName("ScoresetJ3")
        self.ScoresetJ3.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.ScoresetJ3)

        self.ScoresetJ2 = QLCDNumber()
        self.ScoresetJ2.setGeometry(CENTER_X-50, CENTER_Y+70, 51, 20)
        self.ScoresetJ2.setObjectName("ScoresetJ2")
        self.ScoresetJ2.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.ScoresetJ2)

        self.ScoresetJ4 = QLCDNumber()
        self.ScoresetJ4.setGeometry(CENTER_X+70, CENTER_Y+70, 51, 20)
        self.ScoresetJ4.setObjectName("ScoresetJ4")
        self.ScoresetJ4.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.scene.addWidget(self.ScoresetJ4)


        menu = self.menuBar().addMenu("&Game")
        menu = self.menuBar().addMenu("&Rules")

        self.setCentralWidget(view)
        self.setFixedSize(*WINDOW_SIZE)
        self.setWindowTitle("Tarot")
        self.show()

    def restart_game(self):
        reply = QMessageBox.question(self, "Deal again", "Are you sure you want to start a new game?",
                                      QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.shuffle_and_stack()

    def quit(self):
        self.close()


if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.exec_()