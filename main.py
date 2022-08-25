happiness_total = 0
Happiness_05 = 0
time_of_sickness_unattended_secondsauto_background_refresh = 0
Adult_2 = 0
Adult_1 = 0
Adult = 0
happiness_average = 0
_2_days_in_milliseconds = 0
Time_last_eaten_in_seconds = 0
sick_0_is_no_1_is_yes = 0
Hunger_0_is_very_hungry_5_is_not_hungry = 0
Time_of_poo_left_unattended_in_seconds = 0
poo_0_is_no_1_is_yes = 0
Age_of_pet_in_secondsauto_background_refresh = 0
Health_0_is_dead_5_is_max = 0
if tinkercademy.ad_keyboard(ADKeys.A, AnalogPin.P1):
    Health_0_is_dead_5_is_max = 5
    Age_of_pet_in_secondsauto_background_refresh = 0
    poo_0_is_no_1_is_yes = 0
    Time_of_poo_left_unattended_in_seconds = 0
    Hunger_0_is_very_hungry_5_is_not_hungry = 0
    sick_0_is_no_1_is_yes = 0
    basic.show_string("Hatch soon")
    for index in range(30):
        basic.pause(100)
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . . . #
                        # . . . #
                        . # # # .
        """)
    basic.show_string("Hatched")
    Time_last_eaten_in_seconds = 0

def on_forever():
    global Adult
    basic.pause(_2_days_in_milliseconds)
    for index2 in range(100):
        music.play_melody("C5 G E C F A C5 D ", 20867)
    if happiness_average >= 30:
        Adult = Adult_1
    else:
        Adult = Adult_2
basic.forever(on_forever)

def on_forever2():
    global Time_last_eaten_in_seconds, Hunger_0_is_very_hungry_5_is_not_hungry
    if tinkercademy.ad_keyboard(ADKeys.C, AnalogPin.P1):
        Time_last_eaten_in_seconds = 0
        Hunger_0_is_very_hungry_5_is_not_hungry = 5
basic.forever(on_forever2)

def on_forever3():
    global Time_of_poo_left_unattended_in_seconds, sick_0_is_no_1_is_yes
    if poo_0_is_no_1_is_yes == 1:
        basic.show_icon(IconNames.DUCK)
    while poo_0_is_no_1_is_yes == 1:
        basic.pause(100)
        Time_of_poo_left_unattended_in_seconds += 1
    if Time_of_poo_left_unattended_in_seconds > 1019999.9994:
        sick_0_is_no_1_is_yes = 1
basic.forever(on_forever3)

def on_forever4():
    global Hunger_0_is_very_hungry_5_is_not_hungry
    if Time_last_eaten_in_seconds >= 8280000:
        for index3 in range(randint(0, 20)):
            basic.pause(1000)
        while Time_last_eaten_in_seconds >= 8280:
            basic.pause(1800000)
            Hunger_0_is_very_hungry_5_is_not_hungry += -1
basic.forever(on_forever4)

def on_forever5():
    if Adult == Adult_1:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
        """)
basic.forever(on_forever5)

def on_forever6():
    global Time_last_eaten_in_seconds
    basic.pause(100)
    Time_last_eaten_in_seconds += 1
basic.forever(on_forever6)

def on_forever7():
    global Age_of_pet_in_secondsauto_background_refresh
    basic.pause(100)
    Age_of_pet_in_secondsauto_background_refresh += 1
basic.forever(on_forever7)

def on_forever8():
    if Hunger_0_is_very_hungry_5_is_not_hungry <= 3:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        # # # # #
                        . # # # .
                        . . . . .
        """)
        for index4 in range(3):
            music.play_melody("G G G G G G G G ", 999)
basic.forever(on_forever8)

def on_forever9():
    global poo_0_is_no_1_is_yes, Time_of_poo_left_unattended_in_seconds, time_of_sickness_unattended_secondsauto_background_refresh, sick_0_is_no_1_is_yes
    if tinkercademy.ad_keyboard(ADKeys.B, AnalogPin.P1):
        poo_0_is_no_1_is_yes = 0
        Time_of_poo_left_unattended_in_seconds = 0
        time_of_sickness_unattended_secondsauto_background_refresh = 0
        sick_0_is_no_1_is_yes = 0
basic.forever(on_forever9)

def on_forever10():
    global Happiness_05, happiness_total
    if tinkercademy.ad_keyboard(ADKeys.D, AnalogPin.P1):
        Happiness_05 += 1
        happiness_total += 1
basic.forever(on_forever10)

def on_forever11():
    global time_of_sickness_unattended_secondsauto_background_refresh, Time_last_eaten_in_seconds
    if sick_0_is_no_1_is_yes == 1:
        while sick_0_is_no_1_is_yes == 1:
            music.play_melody("A - A - A - C5 - ", 1300)
        while sick_0_is_no_1_is_yes == 1:
            basic.show_leds("""
                # . # . #
                                . # . # .
                                # . # . #
                                . # . # .
                                # . # . #
            """)
            basic.pause(100)
            time_of_sickness_unattended_secondsauto_background_refresh += 1
        if time_of_sickness_unattended_secondsauto_background_refresh > 180000:
            Time_last_eaten_in_seconds += -1
basic.forever(on_forever11)

def on_forever12():
    global poo_0_is_no_1_is_yes
    if Time_last_eaten_in_seconds >= 1800000:
        poo_0_is_no_1_is_yes = 1
basic.forever(on_forever12)

def on_forever13():
    while Health_0_is_dead_5_is_max == 0:
        basic.show_leds("""
            . # # # .
                        # . # . #
                        # # # # #
                        . # # # .
                        . # . # .
        """)
        for index5 in range(3):
            music.play_melody("D C5 C5 C5 C5 C5 C5 C5 ", 394)
basic.forever(on_forever13)

def on_forever14():
    if Adult == Adult_2:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # # # # #
                        . . . . .
        """)
basic.forever(on_forever14)

def on_forever15():
    global happiness_average
    happiness_average = happiness_total / Age_of_pet_in_secondsauto_background_refresh
basic.forever(on_forever15)

def on_forever16():
    global Health_0_is_dead_5_is_max
    if Hunger_0_is_very_hungry_5_is_not_hungry == 0:
        while Hunger_0_is_very_hungry_5_is_not_hungry == 0:
            basic.pause(1800000)
            Health_0_is_dead_5_is_max += -1
basic.forever(on_forever16)

def on_forever17():
    global _2_days_in_milliseconds
    _2_days_in_milliseconds = 172000000
basic.forever(on_forever17)
def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

emptyObstacleY = 0
ticks = 0
bird: game.LedSprite = None
index = 0
obstacles: List[game.LedSprite] = []
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)

def on_forever():
    global emptyObstacleY, ticks
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
    for obstacle2 in obstacles:
        obstacle2.change(LedSpriteProperty.X, -1)
    if ticks % 3 == 0:
        emptyObstacleY = randint(0, 4)
        for index2 in range(5):
            if index2 != emptyObstacleY:
                obstacles.append(game.create_sprite(4, index2))
    for obstacle3 in obstacles:
        if obstacle3.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y):
            game.game_over()
    ticks += 1
    basic.pause(1000)
basic.forever(on_forever)