# -*- coding: utf-8 -*-

# TODO 01
'''
import các thư viện cần dùng
pygame: đồ hoạ game
time: lấy và xử lý giá trị thời gian
random: phát sinh số ngẫu nhiên
'''

# END TODO 01

pygame.init()

# TODO 02
'''
khai báo các biến tương ứng với các màu theo RGB với cấu trúc tuple
white   255, 255, 255
yellow  255, 255, 102
black   0, 0, 0
red     213, 50, 80
green   0, 255, 0
blue    50, 153, 213
'''

# END TODO 02

# TODO 03
'''
khai báo hai biến dis_width, dis_height tương ứng với kích thước
cửa sổ game 600, 400
'''

# END TODO 03

dis = pygame.display.set_mode((dis_width, dis_height))

# TODO 04
'''
dùng lệnh pygame.display.set_caption() để đặt title cho cửa sổ game
'''

# END TODO 04

clock = pygame.time.Clock()


# TODO 05
'''
khai báo hai biến snake_block và snake_speed tương ứng với
kích thước (pixel) cạnh ô vuông tạo nên snake và tốc độ di
chuyển (pixel/clock)
VD: 10 pixel và 15 pixel/clock
'''

# END TODO 05

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    # TODO 06
    '''
    khai báo chuỗi ký tự text để hiển thị điểm lên màn hình với score
    là tham số được truyền vào hàm
    VD: 'scores: 10'
    '''
    text = ''
    # END TODO 06
    value = score_font.render(text, True, yellow)
    dis.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def showMessage(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    # vị trí ban đầu của snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    # toạ độ ban đầu của food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            showMessage("Press C-Play Again or Q-Quit", red)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # TODO 07
                    '''
                    nếu event.key là pygame.K_q thì thay đổi
                    game_over thành True
                    game_close thành False
                    '''

                    # END TODO 07
                   
                    # TODO 08
                    '''
                    nếu event.key là pygame.K_c thì gọi hàm gameLoop()
                    '''

                    # END TODO 08

        for event in pygame.event.get():
            # TODO 09
            '''
            nếu event.type là pygame.QUIT thì gán
            game_over thành True
            '''

            # END TODO 09

            if event.type == pygame.KEYDOWN:
                # TODO 10
                '''
                nếu event.key là pygame.K_LEFT
                thì gán x1_change thành -snake_block, y1_change thành 0

                ngược lại nếu event.key là pygame.K_RIGHT
                thì gán x1_change thành snake_block, y1_change thành 0

                ngược lại nếu event.key là pygame.K_UP
                thì gán x1_change thành 0, y1_change thành -snake_block

                ngược lại nếu event.key là pygame.K_DOWN
                thì gán x1_change thành 0, y1_change thành snake_block
                '''

                # END TODO 10
                pass

        # TODO 11
        '''
        nếu hoành độ x1 của snake vượt quá chiều ngang cửa sổ hoặc âm
        hoặc tung độ y1 của snake vượt quá chiều cao cửa sổ hoặc âm
        thì gán game_close thành True.
        '''

        # END TODO 11
        
        # TODO 12
        '''
        tăng x1 một lượng x1_change
        tăng y1 một lượng y1_change
        '''

        # END TODO 12
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # TODO 13
        '''
        khai báo snake_head là toạ độ x1, y1 dạng tuple
        '''
        snake_head = None
        # END TODO 13
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # TODO 14
        '''
        kiểm tra xem snake có va vào thân của mình không?
        gợi ý: kiểm tra snake_head có trùng với điểm nào trong
        snake_list (nhớ bỏ qua phần tử cuối cùng)

        nếu có gán game_close thành True
        '''

        # END TODO 14

        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)
        pygame.display.update()

        # TODO 15
        '''
        nếu toạ độ x1, y1 trùng với foodx, foody thì snake ăn food và tăng độ dài lên 
        1 đơn vị, sau đó phát sinh điểm food mới. 
        '''
        if None:
            # ...

            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            pass
        # END TODO 15

        clock.tick(snake_speed)

    # nếu vòng lặp while ngừng lại thì thoát game và thoát chương trình
    pygame.quit()
    quit()

# gọi thực thi hàm gameLoop để game bắt đầu.
gameLoop()