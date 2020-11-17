label morning:
    stop music fadeout 3.0
    play ambience ambienceday
    scene bg black with dissolve
    $ renpy.pause (1)
    if livingwithmoxie == 1:
        scene bg moxiebedday with dissolve
    elif livingwithbutters == 1:
        scene bg buttersbedday with dissolve
    else:
        pass
    $ rand = renpy.random.randint(1,10)
    if rand == 1:
        "Я проснулся, отлично выспавшись."
    elif rand == 2:
        "Еще один влажный сон, это место достает меня."
    else:
        "Ахх, очередное утро."
    $ rand = renpy.random.randint(1,3)
    if rand == 1:
        "Я выползаю из кровати и тянусь." #  I crawl out of bed and stretch.
    elif rand == 2:
        "После ещё пяти минут дрема, я встаю с кровати и иду принимать душ." # After five more minutes of snooze time, I get out of bed and go to shower.
    else:
        "*Зевок* Полагаю время вставать с постели." # *Yawwwn...* Guess it's time to get out of bed.
    jump afteraltmorning
    label altmorning:
        stop music
        if livingwithmoxie == 1:
            scene bg moxiewagonday with dissolve
            if fr == 1:
                $ rand = renpy.random.randint(1,3)
                if rand == 1:
                    show moxie walthappy with dissolve
                    moxie "Доброе утро, я была готова вырубиться в любой момент. Уроки Селены были реально тяжелы!"
                    # Good morning, I was just about to go for a nap. Selene's lessons were really tough!
                    moxie "Увидимся позже этой ночью" # See ya later tonight.
                elif rand == 2:
                    "Мокси выглядела сейчас спящей. Она часто спала после полудня от своих вечерних занятий."
                    # Looks like Moxie is asleep right now. She often sleeps into the afternoon with her evening lessons.

                else:
                    show moxie whorny with dissolve
                    moxie "Посмотрите кто решил наконец-то показаться! Хахахах, ты ещё тот фраер."
                    # Look who decided to finally show up! Hahah, you're such a player.
                    mc "Ты же знаешь меня, Я не могу сказать \"нет\". "
                    # You know me, I can't say no."
                    moxie "Это чертовски верно! Вот так ты и я закончили брачные танцы."
                    #  ??? That's heckin' true! That's how you and I ended up rutting.
                    moxie "Раз уж ты не можешь сказать нет, как насчет по-быстрому сделать дела перед тем, как я вздремну, а ты продолжишь работать?"
                    #
                    mc "Ты в деле!" # Как пожелаешь! (???)
                    #
                    scene bg moxiebedday with dissolve
                    show moxie doggystyle1 with dissolve
                    scene bg black with dissolve
            else:
                $ rand = renpy.random.randint(1,10)
                if rand <5:
                    show moxie2 althappy with dissolve
                    moxie "Ох хэй! Рада была увидеть тебя перед тем, как я ушла на работу, я просто свалила."
                    #
                    mc "Хия Мокси, увидеть твою ухмылку - отличный способ начать любой день. Увидимся вечером?"
                    #
                    show moxie2 laughing with dissolve
                    moxie "Увидимся вечером!"
                    "Мы обнимаемся и она гладит меня по заднице."
                    #
                    #
                    hide moxie with dissolve
                elif rand == 10:
                    show moxie happy with dissolve
                    moxie "Как раз тот человек, которого я надеюсь увидеть!"
                    #
                    mc "Эй Мокси, как дела?"
                    #
                    moxie "Тебя не было всю ночь, так что ты вероятно захочешь принять душ, верно?"
                    #
                    mc "Конечно."
                    #
                    moxie "Хорошо, я как раз собиралась принять душ, так как насчет этого?"
                    #
                    mc "Звучит целесообразно."
                    #
                    moxie "елесообразно - это не то слово, которое я бы использовала... Подходи, подходи!"
                    # Ц
                    hide moxie with dissolve
                    "Мы ебалися в душе перед тем как она ушла работать."
                    #
                    scene bg black with dissolve
                elif rand >=5:
                    "Похоже на то, что Мокси уже ушла."
                    #
            pass
        elif livingwithbutters == 1:
            scene bg buttershouse with dissolve
            show butters dresshappy with dissolve
            $ rand = renpy.random.randint(1,3)
            if rand == 1:
                butters "Утро доброе! Полагаю мне лучше привыкнуть к тому, что мистер Популярный не появляется по ночам."
                #
                mc "Хех, может быть. Я собираюсь принять душ."
                #
                butters "Оки-доки, он весь твой."
                #
            elif rand == 2:
                butters "Здравствуй [playername]! Я почти начала готовить вкусный завтрак, если ты примешь душ сейчас он должен быть готов когда ты закончишь."
                #
                mc "Ох идеально, спасибо Баттерс."
                #
            elif rand == 3:
                butters "С возвращением, надеюсь ты не слишком много развлекался без меня, хехе. Моя суккубская сторона может и приревновать."
                #
            scene bg buttershouse with dissolve
        else:
            pass
    label afteraltmorning:
        pass
label morningvariables:
    ## Daytime Variables Reset ## Every morning has to pass this ##
    $ days += 1
    $ dawntalk = 0
    if butterspregnanteasteregg > 0:
        $ butterspregnanteasteregg += 1
    if farmvisit3 == 1:
        $ annamilking += 1
    if butterspregnant == 1:
        $ butterspregnant = 2
    if galleryypass == 1:
        $ galleryyear += 1
        if galleryyear == 365:
            "..."
            "Черт, мой пропуск в галерею просроен."
            "Говорил тебе, что это произойдет."
            #
            #  / Я же предупреждал
            $ galleryypass = 0
    $ pauroras = 0
    $ cindysex = 0
    $ arisextoday = 0
    $ sexwithrubytoday = 0
    $ gallerydpass = 0
    $ augustasex = 0
    $ blossomvisit = 0
    $ melodyvisit = 0
    $ lilytalks = 0
    $ honeycrispsex = 0
    $ rubysex = 0
    $ lilysex = 0
    $ spaspecial = 0
    $ spavisited = 0
    $ penelopetalks = 0
    $ auroratalk = 0
    $ selenetalk = 0
    $ aurorasex = 0
    $ selenesex = 0
    $ honeycrisptalks = 0
    $ blossomtalks = 0
    $ rubytalks = 0
    $ melodytalks = 0
    $ surprisetalks = 0
    $ creamsex2 = 0
    $ creamtalks = 0
    $ creamsex = 0
    $ prismatalks = 0
    $ prismasex = 0
    $ rikutalks = 0
    $ rikusex = 0
    $ moxietalks = 0
    $ lilytalks = 0
    $ sundownertalks = 0
    $ butterstalks = 0
    $ succbutterstalks = 0
    $ poyotalks = 0
    $ blossomsex = 0
    $ annatalks = 0
    $ prismamoxiethreesome = 0
    $ musicstudiotalk = 0
    $ musicstudiosex = 0
    $ persistent.morrigan = 0
    if fr == 1:
        $ worldmap = 3
    else:
        $ worldmap = 1
    if annamilking == 8:
        $ annamilking = 0

    ### Mail
label mail:
    hide moxie with dissolve
    if days >= 20 and bakeryvisits >= 1 and libraryvisit3 == 1 and auroravisitsetup == 0:
        $ auroravisitsetup = 1
        "У меня очередное магическое письмо, обычно для меня это редкость получать одно из них."
        #
        "У меня очередное письмо от Королевы Авроры! Я бы предположил, что она слишком занята, чтобы даже думать обо мне."
        #
        "Наоборот, она непосредственно приглашает меня посетить её в замке."
        #
        "Должен ли идти сейчас?"
        #
        menu:
            "Да":
            #
                jump auroravisit1
            "Не, У меня есть дела. (Посетить её лично в замке)":
            #
                pass
    if days == 3:
        "Похоже у меня магическая почта, это специальный тип письма с крыльями, что автоматически доставляют себя."
        #
        "Вух! Это от Королевы Авроры! Оно даже имеет причудливая печать."
        #
        if augustavisit == 2:
            "I wonder if this is about yesterday?"
            #
            "Я робко разворачиваю письмо и читаю его."
            #
            "'Приветствую [playername]'"
            "It's weird how she knows about me. She even called me by name yesterday, what's up with that?"
            # Это странно, откуда она знает меня. Она даже звала меня по имени вчера?
        else:
            "Я робко разворачиваю письмо и читаю его."

            "'Приветствую [playername]'"
            "Она знает мое имя?"
        "'Ваше присутствие в Аркадии было отмечено; к этому письму прилагается краткое изложение различных законов и культурных различий, которые помогут вам встроиться в мир.'"
        if augustavisit == 2:
            "'Пожалуйста, ведите себя прилично, я надеюсь официально представиться вам в ближайшее время. Прошу прощения за краткий инцидент с Августой."
            "Пожалуйста, найдите владельца библиотеки, Лили, и поговорите с ней.'"
        else:
            "'Пожалуйста, ведите себя прилично, Я надеюсь встретиться с вами когда-нибудь, если возможно. Пожалуйста, найдите владельца библиотеки, Лили, и поговорите с ней.'"
            "Как странно, но мило. Богиня земли прислала мне посылку."
            "Здесь даже есть печенье, \"испеченное сегодня утром специально для тебя\"."
            "Спасибо, Аврора, остальное я прочитаю позже."
            "Прямо сейчас мне нужно быть готовым к работе."
    elif days == 5:
        "Я думаю это выходной, но Аркадия не использует ту же недельную систему, как мой старый мир."
        "Действительно, в такой старомодной местности, как Аркадия, выходных не бывает, давайте приступим к работе."
    elif days == 7:
        "Я уже нахожусь здесь неделю, признаюсь, время прошло быстро."
        "Почти каждый день я занимался чем-то сумашедшим и восхитительным."
        "Еще один дикий день!"

    elif days == 14:
        "Уже прошло две недели с того момента, когда я прибыл! Не быстро ли летит время?"
        "Интересно, какое захватывающее приключение мне предстоит сегодня."
    elif days == 31:
        "Я думаю это месяц, здесь есть календарь, но я не уделил ему достаточно внимания как следовало бы."
        "Что за месяц это был, жить здесь стало таким естесственным как и моя прошлая жизнь. На самом деле я с трудом могу вспомнить, какой была моя жизнь до этого."

        "Я не могу представить себе никакой жизни, кроме той, которой живу сейчас."
        "Это странное ощущение, но я знаю, что я просыпаюсь каждое утро, чтобы с нетерпением встретить день."
    if auroravisit1 == 1 and selenevisit1 == 1 and boutiquevisit3 == 1 and farmvisit3 == 1 and barvisit2 == 1 and fr == 0:
        jump finalroute
    if annamilking == 7:
        "Сегодня день, когда Анну доят в сарае, может мне стоит сходить на ферму повеселиться."
        "Если я это пропущу, мне придется ждать еще одну неделю."
    scene bg black with dissolve
    if dawnvisit == 1 and libraryvisit3 == 1 and dawnltr == 0:
        $ dawnltr = 1
        play ambience ambienceday
        if livingwithmoxie == 1:
            scene bg moxiewagonday with dissolve
        elif livingwithbutters == 1:
            scene bg buttershouse with dissolve
        "А, у меня есть почта… Посмотрим…"
        "’Привет Котеночек’, ах, это от Доун."
        "Стоп, это от Доун?! Как она получила мой адрес?"
        dawn "’Я нуждаюсь в красивом мужчине как ты, и ты можешь быть единственным кто сможет удовлетворить мои срочные желания.’"
        dawn "’Пожалуйста, посетите Ложе Хаоса, когда вам это будет удобно, и я сделаю это более чем стоящим вашего времени ...’"
        "Для этой девушки все - намеки?"
        "Несмотря на предлог, она явно не просит секса, однако такое чувство, что она использует свою сексуальность, чтобы заставить меня танцевать у нее на ладони."
        "Сказав это, я не могу отказаться."
        "Что ж, сейчас утро. Так что мне придется подождать до вечера, прежде чем я пойду к ней."
    if dawnvisit == 3 and dawnltr == 1 and fr == 1:
        $ dawnltr = 2
        play ambience ambienceday
        if livingwithmoxie == 1:
            scene bg moxiewagonday with dissolve
        elif livingwithbutters == 1:
            scene bg buttershouse with dissolve
        "Хм! У меня магическое письмо… Давайте посмотрим."
        "’Привет, мой маленький котенок! У меня особая любовная работа, которую может выполнить только мужчина твоих способностей. Приходите ко мне, подойдет любое утро. Чао, утенок!"
        "Эй, на этот раз она назвала меня котенком и утенком одновременно. Интересно, использует ли она и то, и другое для разнообразия."
        "Я более чем счастлив снова встретиться с этой девушкой, мне нужно пойти как можно скорее."

label events:
    ### events
    if moxieroses == 1 and honeyrubythreesome == 1 and melodylaptop == 1 and doggirl1 == 1 and wolfgirl1 == 1 and midnasexd == 1:
        pass
        if zoe == 2 and arisex == 1 and dawnvisit >= 4 and spaday == 0:
            pass
            if sofiasex == 1 and aure == 0 and sdps == 1 and buttersroses == 1 and cindylum == 1 and spatodo >= 2 and fr == 1:
                $ spaday = 1
                if livingwithbutters == 1:
                    scene bg buttershouse with dissolve
                    play ambience ambienceday
                    show butters dresshappy with d
                    butters "Доброе утро. Я получила волшебное письмо от Лили, которая приглашает нас с тобой в сауну, чтобы отдохнуть на открытом воздухе."
                    butters "Кажется, приглашены все, кто был связан с Морриган, и королевские сестры организовали это сами."
                    mc "Круто, когда мы можем идти?"
                    butters "Письмо говорит встретиться в замке. Должны ли мы идти сейчас?"
                else:
                    scene bg moxiewagonday with dissolve
                    show moxie whappy with d
                    moxie "Доброе утро, тигр! Я только что получила волшебное письмо от Лили, которая приглашает нас в сауну под открытым небом. Похоже, прекрасная возможность расслабиться"
                    moxie "И приглашены почти все участники недавнего инцидента с Морриган! Королевские сестры организовали его сами."
                    mc "Круто, когда мы можем идти?"
                    moxie "Письмо говорит встретиться в замке. Хочешь выйти сейчас?"

                "(100%% бонус завершения разблокирован в Замке.)"
                "(Активация этого бонуса завершает игру, обязательно заранее сделайте дополнительное сохранение.)"
                $ worldmap = 3
                jump prefinalworldmap
    pass
    if livingwithmoxie == 1:
        scene bg moxiewagonday with dissolve
    elif livingwithbutters == 1:
        scene bg buttershouse with dissolve
        play ambience ambienceday
        if butterspregnanteasteregg >= 60:
            jump butterspregnanteasteregg
        if butterspregnant == 2:
            $ butterspregnant = 3
            jump buttersimpregpaizuri
        if buttersimpregintro == 0 and buttersgifts > 1:
            show bg buttershouse with dissolve
            $ buttersimpregintro = 1
            jump buttersimpregintro
        ###
        $ rand = renpy.random.randint(1,2)
        if rand == 1:
            "Я закончил мыться и есть завтрак. Когда я закончил, Баттерс оделась и присоединилась ко мне в гостинной."
            #
        elif rand == 2:
            "Я делаю утренние дела и завтракаю с Баттерс."
            #
        $ rand = renpy.random.randint(1,3)
        if rand == 1:
            show butters succubus with dissolve
            "Кто, кстати, превратился в суккуба снова."
            #
            $ rand = renpy.random.randint(1,2)
            if rand == 1:
                butters "Надеюсь я не единственная, кто проснулся в утреннем лесу."
            elif rand == 2:
                butters "Это нормальная еда отстой, Я хочу немного кончи!"
            jump butterssuccmenu
        else:
            show butters dresshappy with dissolve
            $ rand = renpy.random.randint(1,3)
            if rand == 1:
                butters "Есть планы на сегодня?"
            elif rand == 2:
                butters "Я живу в нескольких минутах, дай мне знать если хочешь исследовать пещер со мной."
                #
            else:
                butters "Я всегда люблю утро."
            jump buttersnormalmenu
    else:
        pass
    $ rand = renpy.random.randint(1,3)
    if rand == 1:
        "Я делаю утреннюю рутину и выхожу."
    elif rand == 2:
        "После завтрака, я готов идти работать. Где бы это ни было сегодня."
        #
    else:
        "Так, на это утро почти все сделано. Куда сегодня?"
        #
    if buttersthirdvisitsetup == 1:
        $ buttersthirdvisitsetup = 0
        jump forestvisit3
    if fr == 1:
        $ worldmap = 3
        jump prefinalworldmap
    $ worldmap = 1
    jump preworldmap
