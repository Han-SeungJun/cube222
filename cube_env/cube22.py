from abc import ABC, abstractmethod, ABCMeta
import wx
import random
import sqlite3 as sq

MIX_NUM = 60
TIME = 0.01

class Cube2(metaclass = ABCMeta):
    
    def __init__(self, mix_num = MIX_NUM, time = TIME):
        self.mix_num = MIX_NUM
        self.time = TIME
        self.ROTATION_COUNT = 0
        self.ROTATION_SEQUENCE = []
        self.myCube = [[[1, 2, 3], [1, 3, 4], [1, 5, 2], [1, 4, 5]],
                  [[6, 3, 2], [6, 4, 3], [6, 2, 5], [6, 5, 4]]]
    
    @abstractmethod
    def createCube(self):
        """큐브 환경을 조성"""
        pass
    
    @abstractmethod
    def cleanCube(self):
        """큐브를 처음 상태로 되돌린다."""
        pass
    
    @abstractmethod
    def elementClockwise(self, floor, piece):
        """큐브의 모서리조각을 시계방향으로 돌려준다.
        입력방식 : elementClockwise(floor, piece)"""
        pass
    
    @abstractmethod
    def elementCounterclockwise(self, floor, piece):
        """큐브의 모서리조각을 반시계방향으로 돌려준다.
        입력방식 : elementCounterclockwise(floor, piece)"""
        pass
    
    @abstractmethod
    def upRight(self):
        """윗면을 시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def upLeft(self):
        """윗면을 반시계 방향으로 회전한다."""
        pass
    
    @abstractmethod
    def downRight(self):
        """아랫면을 시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def downLeft(self):
        """아랫면을 반시계 방향으로 회전한다."""
        pass
    
    @abstractmethod
    def rightRight(self):
        """오른쪽 면을 시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def rightLeft(self):
        """오른쪽 면을 반시계 방향으로 회전한다."""
        pass
    
    @abstractmethod
    def leftRight(self):
        """왼쪽 면을 시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def leftLeft(self):
        """왼쪽 면을 반시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def frontRight(self):
        """앞면을 시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def frontLeft(self):
        """앞면을 반시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def backRight(self):
        """"뒷면을 시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def backLeft(self):
        """"뒷면을 반시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def xRight(self):
        """큐브 전체를 앞면 축에 대해 시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def xLeft(self):
        """큐브 전체를 앞면 축에 대해 시계 반대방향으로 회전한다."""
        pass
    
    @abstractmethod
    def yRight(self):
        """큐브 전체를 오른쪽 면의 축에 대해 시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def yLeft(self):
        """큐브 전체를 오른쪽 면의 축에 대해 반시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def zRight(self):
        """큐브 전체를 윗면의 축에 대해 시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def zLeft(self):
        """큐브 전체를 윗면의 축에 대해 반시계방향으로 회전한다."""
        pass
    
    @abstractmethod
    def clearCube(self):
        """큐브 전체를 24가지 경우로 돌려보며 모두 맞춰졌는지 판별하는 함수"""
        pass
    
    @abstractmethod
    def ifClear(self):
        """큐브의 모든 조각들의 요소가 맞춰져있는지 판별하는 함수."""
        pass
    
    @abstractmethod
    def mixCube(self):
        """큐브를 무작위로 섞는다."""
        pass
    
    @abstractmethod
    def saveCube(self):
        """큐브의 상태를 .db 형식 파일에 저장"""
        pass
    
    @abstractmethod
    def loadCube(self):
        """.db 형식 파일에 저장된 큐브 상태를 불러옴"""
        pass
    
    @abstractmethod
    def distColor(self, floor, piece, color):
        """각 큐브 조각의 색을 디코딩"""
        pass
    
    @abstractmethod
    def defColor(self):
        """각 큐브 조각의 값을 색으로 변환"""
        pass
    
    @abstractmethod
    def distNumber(self, floor, piece, color):
        """각 큐브 조각의 색을 데이터로 인코딩"""
        pass
    
    @abstractmethod
    def defNumber(self):
        """각 큐브 조각의 색을 수치로 변환"""
        pass

class realCube(Cube2):
    def createCube(self):
        global sampleCube
        global cubeRegister
        global pieceRegister

        sampleCube = [[[1, 2, 3], [1, 3, 4], [1, 5, 2], [1, 4, 5]],
                      [[6, 3, 2], [6, 4, 3], [6, 2, 5], [6, 5, 4]]]
        cubeRegister = [[None, None, None], [None, None, None],
                        [None, None, None], [None, None, None]]
        pieceRegister = [None, None, None]
        
    def cleanCube(self):
        self.ROTATION_COUNT = 0
        self.ROTATION_SEQUENCE = []
        self.myCube = [[[1, 2, 3], [1, 3, 4], [1, 5, 2], [1, 4, 5]],
                      [[6, 3, 2], [6, 4, 3], [6, 2, 5], [6, 5, 4]]]

    def elementClockwise(self, floor, piece):
        """큐브의 모서리조각을 시계방향으로 돌려준다.
        입력방식 : elementClockwise(floor, piece)"""
        pieceRegister[0:3] = self.myCube[floor][piece][0:3]
        self.myCube[floor][piece][0] = pieceRegister[1]
        self.myCube[floor][piece][1] = pieceRegister[2]
        self.myCube[floor][piece][2] = pieceRegister[0]

    def elementCounterclockwise(self, floor, piece):
        """큐브의 모서리조각을 반시계 방향으로 돌려준다.
        입력방식 : elementCounterclockwise(floor, piece)"""
        pieceRegister[0:3] = self.myCube[floor][piece][0:3]
        self.myCube[floor][piece][0] = pieceRegister[2]
        self.myCube[floor][piece][1] = pieceRegister[0]
        self.myCube[floor][piece][2] = pieceRegister[1]

    def upRight(self):
        """윗면을 시계방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('U')
        cubeRegister[0:4] = self.myCube[0][0:4]
        self.myCube[0][0] = cubeRegister[1]
        self.myCube[0][1] = cubeRegister[3]
        self.myCube[0][2] = cubeRegister[0]
        self.myCube[0][3] = cubeRegister[2]

    def upLeft(self):
        """윗면을 시계 반대방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('U\'')
        cubeRegister[0:4] = self.myCube[0][0:4]
        self.myCube[0][0] = cubeRegister[2]
        self.myCube[0][1] = cubeRegister[0]
        self.myCube[0][2] = cubeRegister[3]
        self.myCube[0][3] = cubeRegister[1]

    def downRight(self):
        """아랫면을 시계방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('D')
        cubeRegister[0:4] = self.myCube[1][0:4]
        self.myCube[1][0] = cubeRegister[2]
        self.myCube[1][1] = cubeRegister[0]
        self.myCube[1][2] = cubeRegister[3]
        self.myCube[1][3] = cubeRegister[1]

    def downLeft(self):
        """아랫면을 시계 반대방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('D\'')
        cubeRegister[0:4] = self.myCube[1][0:4]
        self.myCube[1][0] = cubeRegister[1]
        self.myCube[1][1] = cubeRegister[3]
        self.myCube[1][2] = cubeRegister[0]
        self.myCube[1][3] = cubeRegister[2]

    def rightRight(self):
        """오른쪽 면을 시계방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('R')
        cubeRegister[0:2], cubeRegister[2:4] = self.myCube[0][0:2], self.myCube[1][0:2]
        self.myCube[0][0] = cubeRegister[2]
        self.myCube[0][1] = cubeRegister[0]
        self.myCube[1][0] = cubeRegister[3]
        self.myCube[1][1] = cubeRegister[1]
        self.elementCounterclockwise(0, 0)
        self.elementClockwise(0, 1)
        self.elementClockwise(1, 0)
        self.elementCounterclockwise(1, 1)

    def rightLeft(self):
        """오른쪽 면을 시계 반대방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('R\'')
        cubeRegister[0:2], cubeRegister[2:4] = self.myCube[0][0:2], self.myCube[1][0:2]
        self.myCube[0][0] = cubeRegister[1]
        self.myCube[0][1] = cubeRegister[3]
        self.myCube[1][0] = cubeRegister[0]
        self.myCube[1][1] = cubeRegister[2]
        self.elementCounterclockwise(0, 0)
        self.elementClockwise(0, 1)
        self.elementClockwise(1, 0)
        self.elementCounterclockwise(1, 1)

    def leftRight(self):
        """왼쪽 면을 시계방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('L')
        cubeRegister[0:2], cubeRegister[2:4] = self.myCube[0][2:4], self.myCube[1][2:4]
        self.myCube[0][2] = cubeRegister[1]
        self.myCube[0][3] = cubeRegister[3]
        self.myCube[1][2] = cubeRegister[0]
        self.myCube[1][3] = cubeRegister[2]
        self.elementClockwise(0, 2)
        self.elementCounterclockwise(0, 3)
        self.elementCounterclockwise(1, 2)
        self.elementClockwise(1, 3)

    def leftLeft(self):
        """왼쪽 면을 시계 반대방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('L\'')
        cubeRegister[0:2], cubeRegister[2:4] = self.myCube[0][2:4], self.myCube[1][2:4]
        self.myCube[0][2] = cubeRegister[2]
        self.myCube[0][3] = cubeRegister[0]
        self.myCube[1][2] = cubeRegister[3]
        self.myCube[1][3] = cubeRegister[1]
        self.elementClockwise(0, 2)
        self.elementCounterclockwise(0, 3)
        self.elementCounterclockwise(1, 2)
        self.elementClockwise(1, 3)

    def frontRight(self):
        """앞면을 시계방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('F')
        cubeRegister[0:4] = self.myCube[0][2], self.myCube[0][0], self.myCube[1][2], self.myCube[1][0]
        self.myCube[0][0] = cubeRegister[0]
        self.myCube[0][2] = cubeRegister[2]
        self.myCube[1][0] = cubeRegister[1]
        self.myCube[1][2] = cubeRegister[3]
        self.elementCounterclockwise(0, 2)
        self.elementClockwise(0, 0)
        self.elementClockwise(1, 2)
        self.elementCounterclockwise(1, 0)

    def frontLeft(self):
        """앞면을 시계 반대방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('F\'')
        cubeRegister[0:4] = self.myCube[0][2], self.myCube[0][0], self.myCube[1][2], self.myCube[1][0]
        self.myCube[0][2] = cubeRegister[1]
        self.myCube[0][0] = cubeRegister[3]
        self.myCube[1][2] = cubeRegister[0]
        self.myCube[1][0] = cubeRegister[2]
        self.elementCounterclockwise(0, 2)
        self.elementClockwise(0, 0)
        self.elementClockwise(1, 2)
        self.elementCounterclockwise(1, 0)

    def backRight(self):
        """뒷면을 시계방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('B')
        cubeRegister[0:4] = self.myCube[0][3], self.myCube[0][1], self.myCube[1][3], self.myCube[1][1]
        self.myCube[0][1] = cubeRegister[3]
        self.myCube[0][3] = cubeRegister[1]
        self.myCube[1][1] = cubeRegister[2]
        self.myCube[1][3] = cubeRegister[0]
        self.elementCounterclockwise(0, 1)
        self.elementClockwise(0, 3)
        self.elementClockwise(1, 1)
        self.elementCounterclockwise(1, 3)

    def backLeft(self):
        """뒷면을 시계 반대방향으로 회전한다."""
        self.ROTATION_COUNT += 1
        self.ROTATION_SEQUENCE.append('B\'')
        cubeRegister[0:4] = self.myCube[0][3], self.myCube[0][1], self.myCube[1][3], self.myCube[1][1]
        self.myCube[0][1] = cubeRegister[0]
        self.myCube[0][3] = cubeRegister[2]
        self.myCube[1][1] = cubeRegister[1]
        self.myCube[1][3] = cubeRegister[3]
        self.elementCounterclockwise(0, 1)
        self.elementClockwise(0, 3)
        self.elementClockwise(1, 1)
        self.elementCounterclockwise(1, 3)

    def xRight(self):
        """큐브 전체를 앞면 축에 대해 시계방향으로 회전한다."""
        self.ROTATION_COUNT -= 2
        self.frontRight()
        self.backLeft()
        self.ROTATION_SEQUENCE.pop()
        self.ROTATION_SEQUENCE.pop()

    def xLeft(self):
        """큐브 전체를 앞면 축에 대해 시계 반대방향으로 회전한다."""
        self.ROTATION_COUNT -= 2
        self.frontLeft()
        self.backRight()
        self.ROTATION_SEQUENCE.pop()
        self.ROTATION_SEQUENCE.pop()

    def yRight(self):
        """큐브 전체를 오른쪽 면의 축에 대해 시계방향으로 회전한다."""
        self.ROTATION_COUNT -= 2
        self.rightRight()
        self.leftLeft()
        self.ROTATION_SEQUENCE.pop()
        self.ROTATION_SEQUENCE.pop()

    def yLeft(self):
        """큐브 전체를 오른쪽 면의 축에 대해 시계 반대방향으로 회전한다."""
        self.ROTATION_COUNT -= 2
        self.rightLeft()
        self.leftRight()
        self.ROTATION_SEQUENCE.pop()
        self.ROTATION_SEQUENCE.pop()

    def zRight(self):
        """큐브 전체를 윗면의 축에 대해 시계방향으로 회전한다."""
        self.ROTATION_COUNT -= 2
        self.upRight()
        self.downLeft()
        self.ROTATION_SEQUENCE.pop()
        self.ROTATION_SEQUENCE.pop()

    def zLeft(self):
        """큐브 전체를 윗면의 축에 대해 시계 반대방향으로 회전한다."""
        self.ROTATION_COUNT -= 2
        self.upLeft()
        self.downRight()
        self.ROTATION_SEQUENCE.pop()
        self.ROTATION_SEQUENCE.pop()
        
    def ifClear(self):
        """큐브의 모든 조각들의 요소가 맞춰져있는지 판별하는 함수."""
        if (sampleCube[0][0] == self.myCube[0][0] and sampleCube[0][1] == self.myCube[0][1] and
            sampleCube[0][2] == self.myCube[0][2] and sampleCube[0][3] == self.myCube[0][3] and
            sampleCube[1][0] == self.myCube[1][0] and sampleCube[1][1] == self.myCube[1][1] and
            sampleCube[1][2] == self.myCube[1][2] and sampleCube[1][3] == self.myCube[1][3]):

            return 1
        else:
            return 0

    def clearCube(self):
        """큐브 전체를 24가지 경우로 돌려보며 모두 맞춰졌는지 판별하는 함수"""

        find1 = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
        find2 = [[None, None, None, None], [None, None, None, None]]

        for xy_rotate in range(4):
            for x_rotate in range(4):
                self.xRight()
                if (self.ifClear() == 1):
                    find1[xy_rotate][x_rotate] = 1
                else:
                    find1[xy_rotate][x_rotate] = 0
            self.yRight()

        self.zRight()
        for z_rotate in range(2):
            for x_rotate in range(4):
                self.xRight()
                if (self.ifClear() == 1):
                    find2[z_rotate][x_rotate] = 1
                else:
                    find2[z_rotate][x_rotate] = 0
            self.zRight()
            self.zRight()

        if (find1[0][0] == 1 or find1[0][1] == 1 or find1[0][2] == 1 or find1[0][3] == 1 or
            find1[1][0] == 1 or find1[1][1] == 1 or find1[1][2] == 1 or find1[1][3] == 1 or
            find1[2][0] == 1 or find1[2][1] == 1 or find1[2][2] == 1 or find1[2][3] == 1 or
            find1[3][0] == 1 or find1[3][1] == 1 or find1[3][2] == 1 or find1[3][3] == 1 or
            find2[0][0] == 1 or find2[0][1] == 1 or find2[0][2] == 1 or find2[0][3] == 1 or
            find2[1][0] == 1 or find2[1][1] == 1 or find2[1][2] == 1 or find2[1][3] == 1 or
            find3[0] == 1 or find3[1] == 1):
            return 0
        else:
            return 1

    def mixCube(self):
        self.CUBE_MIX_CEED = random.randint(1, 12)

        if (self.CUBE_MIX_CEED == 1):
            self.upRight()
        elif (self.CUBE_MIX_CEED == 2):
            self.upLeft()
        elif (self.CUBE_MIX_CEED == 3):
            self.downRight()
        elif (self.CUBE_MIX_CEED == 4):
            self.downLeft()
        elif (self.CUBE_MIX_CEED == 5):
            self.rightRight()
        elif (self.CUBE_MIX_CEED == 6):
            self.rightLeft()
        elif (self.CUBE_MIX_CEED == 7):
            self.leftRight()
        elif (self.CUBE_MIX_CEED == 8):
            self.leftLeft()
        elif (self.CUBE_MIX_CEED == 9):
            self.frontRight()
        elif (self.CUBE_MIX_CEED == 10):
            self.frontLeft()
        elif (self.CUBE_MIX_CEED == 11):
            self.backRight()
        elif (self.CUBE_MIX_CEED == 12):
            self.backLeft()

    def saveCube(self):
        """큐브 데이터를 저장하는 함수"""
        con = sq.connect('save_cube.db')
        cursor = con.cursor()

        self.defNumber()

        cursor.execute("""DROP TABLE IF EXISTS pieceAddr""")
        cursor.execute("""CREATE TABLE pieceAddr(Floor int, Position int, Element int)""")

        ElementList = (
            (self.myCube[0][0][0]), (self.myCube[0][0][1]), (self.myCube[0][0][2]),
            (self.myCube[0][1][0]), (self.myCube[0][1][1]), (self.myCube[0][1][2]),
            (self.myCube[0][2][0]), (self.myCube[0][2][1]), (self.myCube[0][2][2]),
            (self.myCube[0][3][0]), (self.myCube[0][3][1]), (self.myCube[0][3][2]),
            (self.myCube[1][0][0]), (self.myCube[1][0][1]), (self.myCube[1][0][2]),
            (self.myCube[1][1][0]), (self.myCube[1][1][1]), (self.myCube[1][1][2]),
            (self.myCube[1][2][0]), (self.myCube[1][2][1]), (self.myCube[1][2][2]),
            (self.myCube[1][3][0]), (self.myCube[1][3][1]), (self.myCube[1][3][2]),
        )

        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 0, ElementList[0]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 1, ElementList[1]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 2, ElementList[2]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 3, ElementList[3]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 4, ElementList[4]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 5, ElementList[5]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 6, ElementList[6]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 7, ElementList[7]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 8, ElementList[8]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 9, ElementList[9]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 10, ElementList[10]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (0, 11, ElementList[11]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 12, ElementList[12]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 13, ElementList[13]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 14, ElementList[14]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 15, ElementList[15]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 16, ElementList[16]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 17, ElementList[17]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 18, ElementList[18]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 19, ElementList[19]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 20, ElementList[20]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 21, ElementList[21]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 22, ElementList[22]))
        cursor.execute("INSERT INTO pieceAddr VALUES(?, ?, ?)", (1, 23, ElementList[23]))

        self.defColor()
        
        cursor.execute("""DROP TABLE IF EXISTS rotationAddr""")
#         cursor.execute("""CREATE TABLE rotationAddr(Rotation_count int, Rotation_sequence TEXT)""")
        cursor.execute("""CREATE TABLE rotationAddr(Rotation_count int)""")
        
        cursor.execute("INSERT INTO rotationAddr VALUES(?)", [self.ROTATION_COUNT])

        con.commit()

        cursor.close()
        con.close()

    def loadCube(self):
        """저장했던 큐브 데이터를 불러오는 함수"""
        con = sq.connect('save_cube.db')
        cursor = con.cursor()

        elementList = []
        for x in range(24):
            elementList.append(x)

        for x in range(24):
            cursor.execute("SELECT Element FROM pieceAddr WHERE Position = '%d'" % x)
            elementList[x] = cursor.fetchone()
        
        x = 0
        for floor in range(2):
            for piece in range(4):
                for color in range(3):
                    self.myCube[floor][piece][color] = elementList[x][0]
                    x += 1

        self.defColor()
        
        cursor.execute("SELECT * FROM rotationAddr")
        self.ROTATION_COUNT = cursor.fetchone()[0]

        con.commit()

        cursor.close()
        con.close()

    def distNumber(self, floor, piece, color):
        """각 큐브 조각의 색을 데이터로 인코딩"""
        if (self.myCube[floor][piece][color] == wx.YELLOW):
            self.myCube[floor][piece][color] = 1
        elif (self.myCube[floor][piece][color] == wx.BLUE):
            self.myCube[floor][piece][color] = 2
        elif (self.myCube[floor][piece][color] == wx.RED):
            self.myCube[floor][piece][color] = 3
        elif (self.myCube[floor][piece][color] == wx.Colour(0, 150, 0, 0)):
            self.myCube[floor][piece][color] = 4
        elif (self.myCube[floor][piece][color] == wx.Colour(250, 125, 0, 0)):
            self.myCube[floor][piece][color] = 5
        elif (self.myCube[floor][piece][color] == wx.WHITE):
            self.myCube[floor][piece][color] = 6
        else:
            return 0

    def defNumber(self):
        """각 큐브조각의 색을 데이터로 변환하는 함수"""
        for floor in range(2):
            for piece in range(4):
                for position in range(3):
                    self.distNumber(floor, piece, position)
                    
    def distColor(self, floor, piece, color):
        """각 큐브 조각의 색을 디코딩"""
        if (self.myCube[floor][piece][color] == 1):
            self.myCube[floor][piece][color] = wx.YELLOW
        elif (self.myCube[floor][piece][color] == 2):
            self.myCube[floor][piece][color] = wx.BLUE
        elif (self.myCube[floor][piece][color] == 3):
            self.myCube[floor][piece][color] = wx.RED
        elif (self.myCube[floor][piece][color] == 4):
            self.myCube[floor][piece][color] = wx.Colour(0, 150, 0, 0)
        elif (self.myCube[floor][piece][color] == 5):
            self.myCube[floor][piece][color] = wx.Colour(250, 125, 0, 0)
        elif (self.myCube[floor][piece][color] == 6):
            self.myCube[floor][piece][color] = wx.WHITE
        else:
            return 0

    def defColor(self):
        """각 큐브조각의 값을 색으로 변환하는 함수"""
        for floor in range(2):
            for piece in range(4):
                for position in range(3):
                    self.distColor(floor, piece, position)
