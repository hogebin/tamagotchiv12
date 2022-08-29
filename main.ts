input.onButtonPressed(Button.A, function () {
    bird.change(LedSpriteProperty.Y, -1)
})
input.onButtonPressed(Button.B, function () {
    bird.change(LedSpriteProperty.Y, 1)
})
let time_of_sickness_unattended_secondsauto_background_refresh = 0
let Adult_2 = 0
let Adult_1 = 0
let happiness_average = 0
let _2_days_in_milliseconds = 0
let happiness_total = 0
let Happiness_05 = 0
let emptyObstacleY = 0
let ticks = 0
let index6 = 0
let bird: game.LedSprite = null
let Time_last_eaten_in_seconds = 0
let sick_0_is_no_1_is_yes = 0
let Hunger_0_is_very_hungry_5_is_not_hungry = 0
let Time_of_poo_left_unattended_in_seconds = 0
let poo_0_is_no_1_is_yes = 0
let Age_of_pet_in_secondsauto_background_refresh = 0
let Health_0_is_dead_5_is_max = 0
let Adult = 0
if (tinkercademy.ADKeyboard(ADKeys.A, AnalogPin.P1)) {
    Adult = 0
    Health_0_is_dead_5_is_max = 5
    Age_of_pet_in_secondsauto_background_refresh = 0
    poo_0_is_no_1_is_yes = 0
    Time_of_poo_left_unattended_in_seconds = 0
    Hunger_0_is_very_hungry_5_is_not_hungry = 0
    sick_0_is_no_1_is_yes = 0
    basic.showString("Hatch soon")
    for (let index = 0; index < 30; index++) {
        basic.pause(100)
        basic.showLeds(`
            . . # . .
            . # . # .
            # . . . #
            # . . . #
            . # # # .
            `)
    }
    basic.showString("Hatched")
    Time_last_eaten_in_seconds = 0
}
basic.forever(function () {
    if (tinkercademy.ADKeyboard(ADKeys.D, AnalogPin.P1)) {
        let obstacles: game.LedSprite[] = []
        index6 = 0
        bird = game.createSprite(0, 2)
        bird.set(LedSpriteProperty.Blink, 300)
        while (obstacles.length > 0 && obstacles[0].get(LedSpriteProperty.X) == 0) {
            obstacles.removeAt(0).delete()
        }
        for (let obstacle2 of obstacles) {
            obstacle2.change(LedSpriteProperty.X, -1)
        }
        if (ticks % 3 == 0) {
            emptyObstacleY = randint(0, 4)
            for (let index22 = 0; index22 <= 4; index22++) {
                if (index22 != emptyObstacleY) {
                    obstacles.push(game.createSprite(4, index22))
                }
            }
        }
        for (let obstacle3 of obstacles) {
            if (obstacle3.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) && obstacle3.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y)) {
                game.gameOver()
            }
        }
        ticks += 1
        basic.pause(1000)
        Happiness_05 += 1
        happiness_total += 1
    }
})
basic.forever(function () {
    basic.pause(_2_days_in_milliseconds)
    for (let index = 0; index < 100; index++) {
        music.playMelody("C5 G E C F A C5 D ", 20867)
    }
    if (happiness_average >= 30) {
        Adult = Adult_1
    } else {
        Adult = Adult_2
    }
})
basic.forever(function () {
    basic.pause(100)
    Age_of_pet_in_secondsauto_background_refresh += 1
})
basic.forever(function () {
    if (poo_0_is_no_1_is_yes >= 1) {
        basic.showIcon(IconNames.Duck)
    }
})
basic.forever(function () {
    if (Time_last_eaten_in_seconds >= 8280000) {
        for (let index = 0; index < randint(0, 20); index++) {
            basic.pause(1000)
        }
        while (Time_last_eaten_in_seconds >= 8280) {
            basic.pause(1800000)
            Hunger_0_is_very_hungry_5_is_not_hungry += -1
        }
    }
})
basic.forever(function () {
    while (Health_0_is_dead_5_is_max == 0) {
        basic.showLeds(`
            . # # # .
            # . # . #
            # # # # #
            . # # # .
            . # . # .
            `)
        for (let index = 0; index < 3; index++) {
            music.playMelody("D C5 C5 C5 C5 C5 C5 C5 ", 394)
        }
    }
})
basic.forever(function () {
    _2_days_in_milliseconds = 172000000
})
basic.forever(function () {
    if (poo_0_is_no_1_is_yes == 1) {
        basic.showIcon(IconNames.Duck)
    }
    while (poo_0_is_no_1_is_yes == 1) {
        basic.pause(100)
        Time_of_poo_left_unattended_in_seconds += 1
    }
    if (Time_of_poo_left_unattended_in_seconds > 1019999.9994) {
        sick_0_is_no_1_is_yes = 1
    }
})
basic.forever(function () {
    if (Adult == Adult_2) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            `)
    }
})
basic.forever(function () {
    if (sick_0_is_no_1_is_yes == 1) {
        while (sick_0_is_no_1_is_yes == 1) {
            music.playMelody("A - A - A - C5 - ", 1300)
        }
        while (sick_0_is_no_1_is_yes == 1) {
            basic.showLeds(`
                # . # . #
                . # . # .
                # . # . #
                . # . # .
                # . # . #
                `)
            basic.pause(100)
            time_of_sickness_unattended_secondsauto_background_refresh += 1
        }
        if (time_of_sickness_unattended_secondsauto_background_refresh > 180000) {
            Time_last_eaten_in_seconds += -1
        }
    }
})
basic.forever(function () {
    if (Hunger_0_is_very_hungry_5_is_not_hungry == 0) {
        while (Hunger_0_is_very_hungry_5_is_not_hungry == 0) {
            basic.pause(1800000)
            Health_0_is_dead_5_is_max += -1
        }
    }
})
basic.forever(function () {
    happiness_average = happiness_total / Age_of_pet_in_secondsauto_background_refresh
})
basic.forever(function () {
    if (Hunger_0_is_very_hungry_5_is_not_hungry <= 3) {
        basic.showLeds(`
            . . . . .
            . # # # .
            # # # # #
            . # # # .
            . . . . .
            `)
        for (let index = 0; index < 3; index++) {
            music.playMelody("G G G G G G G G ", 999)
        }
    }
})
basic.forever(function () {
    if (Adult == Adult_1) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
    }
})
basic.forever(function () {
    basic.pause(100)
    Time_last_eaten_in_seconds += 1
})
basic.forever(function () {
    if (tinkercademy.ADKeyboard(ADKeys.C, AnalogPin.P1)) {
        Time_last_eaten_in_seconds = 0
        Hunger_0_is_very_hungry_5_is_not_hungry = 5
    }
})
basic.forever(function () {
    if (Time_last_eaten_in_seconds >= 1800000) {
        poo_0_is_no_1_is_yes = 1
    }
})
basic.forever(function () {
    if (tinkercademy.ADKeyboard(ADKeys.B, AnalogPin.P1)) {
        poo_0_is_no_1_is_yes = 0
        Time_of_poo_left_unattended_in_seconds = 0
        time_of_sickness_unattended_secondsauto_background_refresh = 0
        sick_0_is_no_1_is_yes = 0
    }
})
