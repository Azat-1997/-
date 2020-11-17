label deepforest:
    if forestmonies == 55:
        menu:
            "Go deep into the forest?"
            "Yeah!":
                jump deepforestvisit
            "No way!":
                if worldmap == 2:
                    jump worldmapnight
                else:
                    jump finalworldmapnight
    else:
        "I don't really have a reason to explore deep into the woods, I might even get lost without proper preparation."
        "It'd be fun in a mysterious and creepy way though... Maybe if I had some more equipment I could go for a small hike around the area to fill an evening."
        if worldmap == 2:
            jump worldmapnight
        else:
            jump finalworldmapnight
label deepforestvisit:
    if zoe == 0:
        $ zoe += 1
        jump zoe1
    elif zoe == 1:
        $ zoe += 1
        jump zoe2
    elif zoe == 2:
        jump zoe2

label zoe1:
    "I’ve never stepped far from Arcadia. Even though there’s an entire brand-new world out there."
    scene bg forestnight with d
    "So, here we go, some deep woods exploration for fun. While I’m out here, I could collect some berries for Butters' potions."
    "But really, I’m not interested in work."
    "I’ve been working almost every day for longer than I can imagine. Sometimes it’s nice to just get some fresh air."
    show bg farm6night1 with d
    "Some peace and quiet under the starlit sky will certainly help relieve some stress."
    if melodyeveningvisit1 == 1:
        "It almost reminds me of my evening walk with Melody."
    show bg forestnight with d
    "I did decide to bring my leather armour, it certainly provides some comfort."
    "Even though I’ve gotten used to walking around on my bare feet, the leather shoes are especially nice in the dark."
    "And a scimitar on my back, just in case, but I’ve yet to find a scenario where I’ve needed to use this. I suppose that's the point."
    if melodyeveningvisit1 == 1:
        "Bringing a weapon is a bit more extreme than my walk with Melody, but it feels nice to have a backup plan."
    else:
        "I know this is just going to be a leisurely walk, but it feels nice to have a backup plan."
    "There’s the usual and fairly clear path towards Butters' cottage, then a clearing. I think I’ll do a horse shoe path that’ll lead me back to clearing, or worst-case scenario Honey’s farm."
    "Between the full moon, and the lights of Arcadia city, it’s almost impossible to get lost between these two landmarks."
    "I stretch and set off. The sound of the chirping crickets being my only accompaniment as I step through the deeper woods."
    play sound movement
    show bg forestnight2 with d
    "There’s the occasional shuffling bush, but that’s easily written off as a woodland critter, of which there are many in this area."
    "In the day, the woods are so peaceful and harmonic. In the dark, it’s seemingly hostile, yet exciting."
    "Rather quickly along my walk, I discover my first curiosity within the woods."
    show bg foresthouse2 with d
    "There’s another clearing, and another cottage that’s not too different from Butters’. It’d make sense that there’d be a few of these built around. Even these deep woods feel tamed with a quaint hospitality."
    "It seems that whoever lives in this one doesn’t seem to be home, so I bypass the cottage and continue onwards."
    show bg farm2night with d
    "When I eventually stumble upon a second clearing with a hill that pokes through the trees, I take the opportunity to climb to the top."
    "The hill is impressive, from here I can just peer over most of the trees, and can even see the two cottages poke through."
    "And while Arcadia village is obscured from this angle, the dizzyingly tall castle continues to dwarf me."
    mc "Ahh… This is nice."
    show bg farm6night1 with d
    "I lay down on the grass and enjoy the soft breeze as I gaze into the stars…"
    "*Rustle, rustle*…"
    "*Whisper, whisper*…"
    show bg farm2night with d
    show lamp1
    with d
    pause 1.0
    show lamp2
    hide lamp1
    with d
    pause 0.5
    "My ears prick slightly, at the sounds of some distant movement. Seems like I’m not the only person that decided to have a small peruse around the woods. I spot the orange light of a lantern to the east of my hill perch."
    show lamp3
    hide lamp2
    with d
    pause 1.0
    scene bg farm2night
    with d
    pause 0.5
    "I half-heartedly keep an eye on the light as it continues ahead ignorant to me, but it does pique my curiosity when it spontaneously turns off, and the once chatty whisperings melt into a silence."
    "Hmm…"
    "I should probably head back."
    show pink with d
    "I crick my neck and stand up, and as I do, a certain sickly-sweet scent hits my nose."
    "*Sniff, sniff*"
    "What a strange and indescribable scent…"
    "I can almost directly pin point the origin too, the same location the lamp went out."
    "Somewhat allured, I follow the tantalizing scent with the justification that anyone carrying a lamp is probably just a friendly anthropomorph."
    "But I’m not as naïve as I once was, I’ve worked with Butters a few times and learnt a lot in our time together. Therefore, I take a cautious approach as I crouch behind some bushes and investigate the smell."
    "This heavy scent, if my experiences with Butters are correct, it’s purposely designed to attract males. But… Why would that scent be relevant to the quiet woods at a time like this?"
    "And that’s when she comes into view."
    show zoeb doggystyle
    show zoe doggystyle1
    with d
    "It’s… a zebra? A zebra anthropomorph!"
    "She isn’t even trying to hide herself, and the contrasting stripes of white on the zebra girl shine in the moonlight."
    "I however, am yet to reveal myself as I crouch behind the bushes."
    "It’s hard to really assume a context for this situation, but I have to assume that she’s waiting for someone, or something…"
    "Especially given that strange scent that attracts males… It’s so effective, that it managed to attract me when I was planning on completely ignoring this. I feel like a bit of a monke brain right now."
    unknown "The time is nigh, now don’t be shy…"
    "Is... is she talking to me?"
    unknown "That’s right big boy, no need for tours, I’m all yours..."
    "She isn’t looking my way, so by all means, she isn’t talking to me…"
    "But… Who, then?"
    unknown "Don’t you want to find a nice place to cum in? I’ll even let you put a thumb in..."
    "Alright, this is getting weird."
    "Just gonna, slowly leave…"
    play sound movement
    "*Rustle, rustle*… !"
    scene bg forestnight with d
    "Something, above me?"
    "Falling out from the trees, none other than Butters nimbly drops before me."
    show butters robeneutral with d
    mc "B-B…! *Whispering* Butters?"
    butters "Phew, it’s just you! Heh, I thought maybe I’d been spotted."
    mc "What’s going on?"
    show butters robehappy with d
    butters "Ah, it must look pretty strange, right?"
    mc "No kidding."
    show butters robeneutral with d
    butters "Well, Zoe over there... she’s hoping to attract a werewolf for some 'fun'. I’m here to moderate, and I have a potion to revert both the lycanthropy of the werewolf, and herself."
    mc "Ah, you’re trying to lure in a werewolf with sex, and then cure them."
    show butters robeangry with d
    butters "Yup. I told Zoe I wouldn’t help her sleep with Mr. Wolfies anymore unless we helped them."
    mc "That’s what this strange bonerific scent is for, then?"
    show butters robeneutral with d
    butters "Yeah, is that what brought you here? Hehe, sorry for tricking you. Usually anthropomorphs can’t smell it unless they’re very close, but a werewolf’s sharp nose can smell it from up to ten kilometres away."
    mc "Ah, it’s fine. I was relaxing on a nearby hill when I saw the glow of your lantern."
    mc "I should have realized it was you, after all, anyone else would probably just use a torch."
    scene zoeb doggystyle
    show zoe doggystyle1
    with d
    zo "Come ooonn, big boyyy… There’s no need to be coy! Take me like the beast you are!"
    mc "Hmm… How long does this usually take?"
    scene bg forestnight
    show butters robeneutral
    with d
    butters "Well, we were going to wait for at least an hour… But…"
    mc "But?"
    show butters robesad with d
    butters "I keep telling her that the full moon already passed during the day, and it’s currently a waning gibbous…"
    mc "The full moon started and stopped during the day?"
    show butters robeneutral with d
    butters "Yeah, it’s a rookie mistake to just assume the moon operates only by nightfall."
    butters "And technically a full moon only lasts within an instant, which causes the werewolf transformation, and then the transformation only lasts a few hours…"
    butters "But she insists, and I can’t really blame her for trying…"
    show butters robehappy with d
    butters "…And… I’m getting paid."
    "She winks and leans back on a tree."
    mc "Your friend sounds stubborn."
    show butters robeneutral with d
    butters "Perhaps stubborn, but also simply hornier than her eyes can see."
    mc "I guess I’ll keep you company."
    scene zoeb doggystyle
    show zoe doggystyle2
    with d
    zo "Uuughh… Butters you were right, I don't think anyone's coming…"
    zo "It’s {i}always{/i} night time in fiction… Just my luck…"
    scene bg forestnight
    show butters robehappy
    with d
    butters "What do you think about Zoe?"
    menu:
        "She seems a little crazy.":
            butters "Anyone that chooses to live in the forest is probably a little crazy."
            butters "And I know the expression is to not stick your dick in crazy, but I heard you should always try it at least once."
            mc "Hmm... You raise good points."
        "She has a really nice ass":
            butters "What do you think would happen if you walked up and told her that right now?"
            mc "Is that a challenge?"
        "I always wanted to bang a Zebra, let's do this!":
            pass
    show butters robelaughing with d
    butters "Hehe, yeah, I think you’re more than capable enough to satisfy her."
    mc "What would she think?"
    show butters robehappy with d
    butters "Hehe, try your luck! I just want to see what her reaction would be to a human!"
    mc "Heh, that does sound amusing. Alright, I’ll do it."
    show butters robelaughing with d
    butters "Okies, if you’re successful, I’ll be up in this tree masturbating if you need me."
    "I don’t know if it’s the strange tantalising aroma making me do this, or the hot zebra ass, but I find myself going along with this strange situation a little easier than anticipated."
    "Dropping my scimitar and leather armour beside Butters and her chosen tree, I step into the opening and catch Zoe’s attention."
    play music sex1 fadein 3.0
    scene zoeb doggystyle
    show zoe doggystyle1
    with d
    zo "Ooohh, you, you’re, you…"
    zo "A male! A male… Perhaps you are looking for someone to nail?"
    mc "A rhyming Zebra?"
    zo "Indeed young man, do you like what you see? I shall offer it to thee."
    "Wiggle wiggle, her butt goes. I choose to play a little hard to get though, crossing my arms and raising an eyebrow."
    "She begins flaunting her pussy like a target, her tail swishing back and forth, while the witches hat she placed on her butt nearly falls off."
    mc "You want it pretty badly, don’t you?"
    zo "Are you not convinced? There’s no trick, I just want dick."
    menu:
        "Alright, get ready for a poundin'":
            pass
        "Once you go Zebra, you'll never go back.":
            pass
        "You must think I stick my dick in any random ass I stumble upon in the woods, don'cha?":
            zo "Only the best of ass here, I am a lady of class."
            mc "A lady of class? Sorry, but if this is 'classy' in this world I'm more out of touch than I realized."
            zo "There is no fear, only a world of pleasure here."
            "I peer behind me for a second while thinking. I bet Butters sent me in here on purpose so she wouldn't have to wait an hour, that's uncharacteristically crafty of her."
            mc "Alright..."
        "And what makes you think I want to give you any? I don't even know who you are.":
            zo "There is no fear, only a world of pleasure here."
            mc "Hmm..."
            "I peer behind me for a second while thinking. I bet Butters sent me in here on purpose so she wouldn't have to wait an hour, that's uncharacteristically crafty of her."
            mc "Alright..."
    mc "But you do have some explaining to do afterwards."
    zo "Absolutely, I shall explain, after I’ve been reined."
    "I could tease her for a few more rhymes, especially since she sometimes takes pause to think of suitable words. Although the ‘rein’ rhyme was pretty genius considering she’s equine. She has probably used that one before."
    mc "If you want it so badly, then I won’t disappoint."
    "As I get into position before her presented rear, she exudes a high level of excitement, her tail swishes so fervently it keeps brushing against me."
    "The sweet flowery aroma that attracted me here combined with the smell of sex heightens my need to pound her pussy, almost to a beguiling degree."
    play sound cum
    show zoe doggystylev1 with d
    "Her drippy pussy is clearly wet and ready, so I skip teasing and begin the session by aligning the tip of my cock against her pussy and pushing inside."
    "Immediately I sink into the pleasant warmth of her depths, her lips parting bit by bit as it easily accepts me to the hilt in a single smooth motion."
    zo "Ahhhh, ahh… I’m so appreciative that you were present, because that feels extremely pleasant."
    play ambience sex fadein 3.0
    "Her hips twitch as I pull back and sink back in, beginning to rut her at a pleasureful pace for the both of us."
    "Zoe was so wet from the start, she was clearly anticipating this and prepared for it. So it’s not too surprising that she accepted me even if I perhaps wasn’t quite what she wanted."
    "The lustful wetness does allow me to pound her as fast as I want though, choosing to alternate between fast thrusting and then slowing myself down as to pace myself."
    "Each movement causes friction against her swollen clit, and deep sensitive spots within her pussy, filling the zebra girl with bliss."
    show zoe doggystylev2 with d
    zo "Aaahhh, haaahhh, that’s it, I want you to fill me with your seed."
    "Hm, she didn’t rhyme that time. I clearly have my priorities wrong if I’m thinking about that right now, but this zebra girl is an enigma to me on so many levels."
    zo "Aahhahah, yesss... That’s good, keep going at that speed!"
    "Oh, there’s the rhyme! I thrust into my lover at the requested pace, rocking her back and forth against the grass while her toes curl and thighs quiver."
    "Doesn’t seem like it’ll take long for her to reach an orgasm, and indeed she does achieve one far before my own, as the mare squeals happily."
    "Her moans grow in lustful intensity, that coupled with the wet schlicking of her pussy, it's pretty much the only thing I can hear as we rut in the dark woods."
    "After her first orgasm, almost impatiently, I feel her own hips begin to rise and fall on my cock. Matching my own pace with some immediacy, and then outmatching it as she speeds up."
    "Her hip movements make her sexual experience immediately clear; she’s done toying around with me, and now she’s going to make me cum."
    "I grab her hips and commit to the accelerating pace, adding a third sound of our bodies slapping together to the mix."
    zo "Ahh, such a sly dog, ahh ahhhh… You’re certainly not a shy lover."
    "My cock begins to twitch and get tighter as my impending orgasm draws closer and closer."
    zo "Now, cum in me, I want it all…"
    "At a certain point my orgasm is all but confirmed, but it still takes a few seconds to escape. I use that time to push my body as far as it’ll go, fucking as hard as I can, to push to the heights of euphoria."
    play sound cum
    show zoe doggystylev3 with cum
    play sound cum
    show zoe doggystylev3 with cum
    "And then in one moment of intense bliss, my cock releases its load deep into the waiting mare."
    play sound cum
    show zoe doggystylev3 with cum
    play sound cum
    show zoe doggystylev3 with cum
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    zo "Ahh, yess, that’s it… Fill up my womb, until there’s simply no room!"
    show zoe doggystylecum with d
    "With one final load of cum, I finally empty my balls into the zebra, and she slumps onto the grass, panting."
    "I follow her example, lying beside her voluptuous breasts."
    "I peek around the tree tops while I’m laid down, but it’s so dark that I can’t make out Butters at all."
    scene bg forestnight
    show zoeb
    show zoe satisfied
    with d
    play ambience ambiencenight fadein 3.0
    "Eventually Zoe stands up and brushes off some stray strands of grass from her fur coat."
    zo "Phew… I was worried no one would come after all. It was certainly a close-call."
    "Right, I already know why she’s here, but she doesn’t know why I’m here. This is a good chance to ask her some questions."
    mc "That was fun, I still have questions though. Care to humour me?"
    show zoe happy with d
    zo "Yes, since you did such an incredible task, I’ll answer anything you ask. My name is Zoe, and you are?"
    mc "Call me [playername], I live nearby in Arcadia. You caught me during an evening adventure."
    show zoe satisfied with d
    zo "Ahh, I see, it's my pleasure, [playername]. Perhaps you saw my humble cottage, I often leave it to indulge in some frottage."
    "Ahh, so she's the occupant of that cottage? I wonder why I've never met her before if she's friends with Butters."
    "Time to pursue this line of questioning further."
    $ zwud = 0
    $ zwit = 0
    $ zbut = 0
    label zoetalkmenu:
        show zoe happy with d
    menu:
        "What were you doing out here?" if zwud == 0:
            $ zwud = 1
            zo "Ahh, mhehe… I was looking for a good time before bedtime, got it?"
            mc "Looking for a good time, in the middle of the woods, with some strange man attracting scent?"
            show zoe horny with d
            zo "It worked, didn’t it? My methods are perhaps unusual, but it gets the job done. This little scent attracts any hun, it’s the perfect fuel."
            mc "True enough, but I have to assume you didn’t get what you wanted."
            show zoe laughing with d
            zo "Perhaps not, but I found you more than enough fun to play around, though I certainly wasn’t expecting anyone from the town."
            zo "In truth, I was hunting for a very specific type of chap. But it would seem I mistimed my little trap."
            mc "Hmph… I feel pretty silly for getting caught up in this."
            show zoe satisfied with d
            zo "Was my pussy not satisfying enough for you? It certainly wringed out enough dew, mhehe."
            mc "I just feel like I ought to stop sleeping with every single thing I see. It’s beginning to get out of hand."
            show zoe neutral with d
            zo "Oh my… Part of the problem, am I?"
            jump zoetalkmenu
        "Are you a Witch?" if zwit == 0:
            $ zwit = 1
            show zoe laughing with d
            zo "A Witch is certainly what some fairy tales could refer to an individual such as myself. However, under the veil, I know no magic."
            show zoe happy with d
            zo "All I know is the mysterious art of alchemy."
            mc "Should you really be telling me that so leisurely? I thought alchemy was a secret."
            show zoe horny with d
            zo "A secret? No. A societal ignorance? Perhaps."
            zo "Most of my care-free customers simply misattribute my wares as not magical, despite the reality."
            zo "Although, that’s because I keep my most magical brews to myself. Some of them are too dangerous to leave the shelf."
            mc "Makes sense that you’d only sell basic wares, then."
            show zoe happy with d
            zo "There are two forest ‘witches’ that you ought to be wary of."
            zo "Mhehe, I kid, we’re very friendly actually. If you visit me again, I may even offer you some more love."
            jump zoetalkmenu
        "Do you know someone called Butters?" if zbut == 0:
            $ zbut = 1
            show zoe neutral with d
            zo "I do indeed, Butters was my alchemical friend. She came to Arcadia initially to work with me in alchemy twenty years ago. Together we can make an impressive blend."
            mc "Hm… That’s longer than I’ve been alive. You don’t mind if I ask, do you?"
            show zoe laughing with d
            zo "My age? I believe someone of your generation may refer to me as a ‘MILF’. I can’t think of a single word that rhymes with MILF, though."
            mc "That’s all I need to know. Hell yeah."
            show zoe neutral with d
            zo "And so, you know of Butters too?"
            mc "Indeed I do, I’m a close friend of hers, actually. I’m surprised you and I haven’t met."
            show zoe angry with d
            zo "How curious. She and I haven’t seen each other much lately, I had accidentally made her furious, and we fell apart."
            mc "Huh? What did you do?"
            show zoe neutral with d
            zo "Mmm, something about werewolves… I needn't bore you with detail."
            mc "Right… I think I get it."
            "I wonder if she gets annoyed if you interrupt her before she finishes her rhyme."
            jump zoetalkmenu
        "(Conclude)":
            pass
    show zoe satisfied with d
    zo "Okay, just as soon as you came out of the blue, now it’s time to shoo."
    mc "You’re telling me to leave?"
    show zoe happy with d
    zo "Would you rather stick around? I have beauty sleep to get. Maybe visit me again at my cottage someday, and we can dick around."
    scene bg forestnight
    show zoeb:
        xpos 150
        ypos 30
    show zoe neutral:
        xpos 150
        ypos 30
    show butters robehappy:
        xpos 550
        ypos 30
    with d
    butters "That’ll be fine, Zoe. I’ll be taking him."
    show zoe angry with d
    zo "Ahh, Butters, you were correct, as usual…"
    show butters robesad with d
    butters "I told you, you were being delusional."
    show zoe neutral with d
    zo "Was this man part of your plan?"
    show butters robeangry with d
    butters "Plan? What are you trying to say? I took part in no scam."
    mc "Oh come on, you can’t both be rhyming with each other."
    show butters robeneutral with d
    butters "Hehe, sorry! I just like playing along sometimes."
    mc "Alright, but why do you do it, Zoe?"
    show zoe laughing with d
    zo "What’s wrong with it, son? Don’t you like to have fun?"
    mc "Bruh… If it requires rhyming every word, I don’t want none."
    show zoe horny with d
    zo "That’s a shame… I loved making you cum."
    show butters robehappy with d
    butters "Alright everyone, it’s getting late. Let's make like a tree and split."
    mc "What a strange walk this turned out to be."
    scene bg forestnight
    show butters robeneutral
    with d
    "Zoe takes her leave, returning in the direction of the other cottage, while Butters and I return to hers."
    scene bg buttershousenight with d
    show butters robeneutral with d
    butters "Ah sheesh… I suppose that was a pretty fun end to the night. Everything is better when you’re involved."
    mc "Is that your old work partner, then? You know, before you and I started to work together a lot."
    mc "I sensed a little bit of tension between you two."
    play sound movement
    show butters sad with d
    "Butters gets changed as she replies."
    butters "Indeed, we worked together for a long time. Although there has been some minor turbulence within our more recent relations. We just can’t seem to agree on anything anymore."
    butters "It’s like she always has something to prove compared to me, an inferiority complex which she self imposes. This leads to her trying to show off, for validation or ego, I couldn't say."
    butters "But the insecurity it brings just leaves her stubborn and standoffish."
    play sound movement
    show butters dressangry with d
    butters "Oh, and that rhyming thing? She just does it for attention. Everyone thinks it’s a funny quirk, but I dunno… To her it’s just another way to try and show off."
    menu:
        "You sound pretty bitter, there must have been something big that made you fall out.":
            show butters dresssad with d
            butters "Well… The last straw for me was the werewolves incident."
            butters "They’re not actually native to this area, she purposely infected someone for her sick fetish!"
        "She doesn’t seem so bad to me.":
            show butters dresssad with d
            butters "Well… Maybe I’m being unfair because I’m currently seeing every aspect of her from a negative light."
            butters "I’ve had a lot of time to dwell on those negatives too, especially because of the recent incident."
            mc "Incident?"
            show butters dressangry with d
            butters "She purposely infected someone with lycanthropy for her sick fetish"
        "I agree, she was so busy trying to rhyme her sentences together that she barely managed to say anything of substance.":
            show butters dresssad with d
            butters "Heh, you meanie… She’s still a really good alchemist, but she’s always been a few pegs behind me, and as a result she’s always tried to out-do me."
            butters "But it’s pretty hard to outdo someone with twice your age and experience."
            butters "I’m fairly sure she can brew her own anti-lycanthropy potions now, but I’m still going to help her cure the werewolves in the area."
            mc "What’s up with the werewolves I keep hearing about?"
            show butters dressneutral with d
            butters "Well… They’re not actually native to this area, she purposely infected someone for her sick fetish"

    mc "Woah, that’s pretty heavy."
    show butters dressangry with d
    butters "I was so pissed off that I swore I’d never work with her again…"
    butters "But here I am, having cured my succubification, so I wanted to try and cure that werewolf too."
    show butters dressneutral with d
    butters "Problem is, there are probably a few of them now…"
    mc "Oh dear! We're all at risk."
    show butters dressangry with d
    butters "Zoe thinks there's just the one male and a few submissive females, but it’s hard to keep track. For all we know, there could be another one from tonight."
    butters "It’s quite the stressful job because it’s almost impossible to identify the curse in regular individuals."
    butters "As long as we can get all the males that’ll typically fix the problem though, female werewolves only mate with other werewolves. But I guess bite infections are still a possiblity..."
    show butters dresssad with d
    butters "So anyway, that’ll be what I do every full moon for about half a year."
    butters "Watching from the trees with two servings of the potion. The only time a werewolf really lets its guard down is when they’re knotted in a female."
    mc "I think I totally understand why you’re pissed off."
    mc "Surprised you let me fuck her, then. You could have just left her to sit around for the hour."
    show butters dresshappy with d
    butters "Ah, I’m not so cruel. I figured you’d still have fun with a thick MILF like her."
    butters "Take her offer to go visit her too, I don’t mind."
    butters "Maybe a normal man will help knock some sense into her."
    mc "Ah-ha! You think if she sleeps with me, she’ll stop being such a werewolf fucker?"
    show butters dresslaughing with d
    butters "Mehh, you’re certainly good enough at sex to take that lustful energy of hers and put it somewhere else."
    mc "Oh well, I don’t mind."
    show butters dresshappy with d
    butters "And thanks for saving about forty-five minutes of my life. Imagine if I had to wait that entire time!"
    mc "Maybe call me next month? Hah."
    if livingwithbutters == 1:
        jump eveningbuttersmenu
    else:
        mc "I’m gonna go back to the wagon. See you later Butters."
        butters "Bye-bye [playername]."
        scene bg black with dissolve
        jump eveningmoxie1
    ###################################################
label zoe2:
    if zoevisit1 == 0:
        $ zoevisit1 = 1
        scene bg forestnight with d
        "Alright, let’s visit the {i}other{/i} witch in the woods."
        "Now that I know a little more about her from Butters, I’m interested to hear if she has a side to this story."
        "I walk through the woods until I stumble upon the second cottage, barely remembering the correct way as I stumble around."
        show bg foresthouse2 with d
        "But eventually, west to Butters’ cottage, I find Zoe’s abode."
        show bg zoehouse with d
        "I knock on the wooden door, and she lets me in."
        show zoeb
        show zoe horny
        with d
        zo "Greetings [playername]. Are you here to give my pussy a beating?"
        mc "Hey Zoe, sheesh, you didn't waste any time. How about you just bend over now why don't you?"
        mc "I suppose by being here I did take you up on that offer though, didn’t I?"
        show zoe satisfied with d
        zo "When I’m done screwing with you, you’ll feel like new."
        "She seductively wiggles her hips, exuding big MILF energy right now."
        mc "I see you’ve taken a liking to me, even though I’m not like your werewolf lovers."
        show zoe angry with d
        zo "Ah, she told you? It’s true, I do like the occasional canine to screw."
        zo "But I suppose you’re not so bad between the full moons. I’d be driven mad if I could only have sex once a month."
        mc "And uh, you made this individual you were hunting for last night a werewolf on purpose?"
        show zoe neutral with d
        zo "Ahh… *Sigh* There was an accident, but Butters claimed I was entirely at fault for my carelessness."
        zo "It’s true, I had a lycanthropy potion… but it was never my intention to give it to someone. Now the curse has spread through sex and biting. It has become quite the stress."
        menu:
            "Butters didn’t seem to think it was an accident…":
                show zoe angry with d
                zo "I empathise with that position. What are the odds that a known wolf fetishist would ‘accidentally’ sell a man an unlabelled lycanthropy potion instead of the product they wanted?"
            "How do you mislabel such an important potion?":
                show zoe angry with d
                zo "Butters had always been critical of my habits, and I always rolled my eyes and acted irate. But she was correct, my habit to not label any of my potions has certainly placed a lot of problems on my plate."
            "Mistakes happen, as long as you try to make amends that’s okay, right?":
                show zoe angry with d
                zo "My actions have caused a lot of grief. The situation should have been far more brief, but my carelessness caused the curse to spread further than it should have."

        show zoe neutral with d
        zo "Yes, I am partially guilty, that is my admission. But it was still an accident, and only recently Butters has come around to see my side of the story, so the two of us tried to cure the victim."
        mc "How many are there?"
        show zoe happy with d
        zo "Hard to say. Our hands are tied due to male werewolves and their predisposition to spread it."
        zo "We’ll need to keep that in bay. When we first met, you saw my method. Using a special pheromone fragrance, we can lure all male werewolves in about a ten-kilometre radius until they just stop coming."
        mc "Uh, what if multiple arrive?"
        show zoe satisfied with d
        zo "I can take a few, then Butters can cure them after they’re exhausted from their screw."
        mc "And the females?"
        show zoe happy with d
        zo "Typically docile and only sought out by the males. Butters is currently trying to concoct a method to detect them, which is great."
        "We should probably get Lily to help, or even Princess Selene. They probably haven't even noticed 2-3 infections, but I bet they can easily nip the problem in the bud."
        zo "If we don’t control the situation, we’ll definitely draw the ire of Princess Selene at this rate. I could do without a prison sentence."
        mc "Hm... I really don't think avoiding help is the solution."
        menu:
            "If you want my advice, it’s time to act real fucking humble, listen to Butters and get this done right.":
                show zoe neutral with d
                zo "*Nods* Yes, this has been a lesson in humility."

            "Whatever man, you deserve this for your carelessness.":
                show zoe neutral with d
                zo "I deserve this? I’m not even the one suffering. It’s them, and they don’t deserve that."

            "Enough about fucking werewolves, how about fucking me instead?":
                show zoe horny with d
                zo "*Sigh* You’re just as bad as they are. But I like a bad boy."

            "Can’t I have a go at a female werewolf if you find one?":
                show zoe neutral with d
                zo "I suppose such a thing could be arranged. Is that something you’re into? I didn’t realize your fetishes were also deranged."

        mc "Hmph…"
        "At that moment, a familiar green figure enters the room."
        scene bg zoehouse
        show alraune neutral:
            xpos 450
            ypos 135
        with d
        alraune "Ah? It’s you!"
        mc "The Alraune from the cave? What are you doing here?"
        show alraune angry with d
        alraune "I live here, dummy!"
        show zoeb:
            xpos 100
            ypos 30
        show zoe happy:
            xpos 100
            ypos 30
        with d
        zo "Mhm, the Alraune here is my pet. She means no threat."
        mc "You know this ‘pet’ molested Butters and I once, right?"
        show zoe angry with d
        zo "Is this true? I shall have to discipline you, Alraune."
        show alraune neutral with d
        alraune "Wha? It was consensual, you bully!"
        alraune "Look, come here [playername]."
        "She comes closer and whispers into my ear."
        show zoe neutral with d
        show alraune horny
        with d
        alraune "*Whisper* Please cut me a break! She’ll be on my ass all month otherwise."
        alraune "*Whisper* I’ll let you bang me if you do!"
        menu:
            "Alright, molestation was a bit of an extreme way to phrase it. We all had a good and consensual time.":
                show alraune laughing with d
                alraune "Yep, yep! What do you think, Zoe?"
                show zoe neutral with d
                zo "Well, I can overlook a small instance of hyperbole from [playername], as long as you were behaving."
                show alraune happy with d
                alraune "Phhhewwww…"

            "Nope, she totally molested us both. She needs some discipline.":
                show zoe angry
                show alraune neutral
                with d
                alraune "Oh come on! It was only some light jovial molestation!"
                mc "There is no such thing!"
                zo "I see… In that case… The only punishment I can think of as an alchemist is one of equivalent exchange."
                zo "Alraune, you must sexually please [playername] to repent. Hopefully one day you can stop acting like an ass, and stop harassing every man you pass."
                "You know, Zoe is really growing on me right now."
                show alraune angry with d
                alraune "Awwwhh maaannn…"
                mc "Why are you complaining? That’s exactly what you said you’d do when you whispered in my ear."
                show alraune neutral with d
                alraune "Yeah but, I hate being told what to do, even if I was gonna do it anyway! Hehe."
        show zoe horny with d
        zo "You seem to be popular in this house, [playername]. Who will you be accompanying tonight?"
    else:
        show bg zoehouse
        show zoeb:
            xpos 100
            ypos 30
        show zoe happy:
            xpos 100
            ypos 30
        with d
        zo "Greetings, [playername]. Always a welcome guest in this household."
        show alraune laughing with dissolve:
            xpos 450
            ypos 135
        if alraunesex == 1 and alraunec == 0:
            $ alraunec = 1
            alraune "Oh my gosh, [playername]! Come here!"
            mc "Huh?"
            "She leads me into her bedroom."
            scene bg poyobedroom with d
            show alraune happy with dissolve
            alraune "Look, our child!"
            mc "Ah?!"
            "She holds out a potted plant towards me. It's a single green stem in some soil."
            mc "Uhh, this thing is our child?"
            show alraune laughing with dissolve
            alraune "Yep! Isn't she soooo cute?"
            mc "Oh, uh, yeah... Is this an Alraune too?"
            show alraune neutral with dissolve
            alraune "Well, she could be in about ten years. For now, it's just a rose!"
            mc "My semen contributed into making a rose? Woah..."
            show alraune happy with dissolve
            alraune "Let's make lots more! Okay?"
            "Man, maybe I oughta be more careful about who I choose to cum in."
            show alraune horny with dissolve
            alraune "For now, um, maybe you want to have some fun with Zoe too? You can pick one of us if you want!"
            scene bg zoehouse
            show zoeb:
                xpos 100
                ypos 30
            show zoe happy:
                xpos 100
                ypos 30
            show alraune laughing:
                xpos 450
                ypos 135
            with d
        else:
            alraune "Hiya! Gonna stay the evening again? You’ll have to pick a lovely lady to spend that time with."
        stop ambience fadeout 20.0

    menu:
        "Sex with Zoe":
            zo "Sorry my dear pet, but [playername] has chosen me today. You needn’t fret, I’m sure you’ll be on his list next."
            alraune "Yeah yeah, whatevs!"
            scene bg zoehouse
            show zoeb
            show zoe horny
            with d
            "Alraune leaves the room, giving us some privacy."
            zo "How would you like to do this?"
            menu:
                "Doggystyle":
                    jump zoedog
                "Leg-up Sideways (NEW!)" if zoelum == 0:
                    jump zoelum
                "Leg-Up Sideways" if zoelum == 1:
                    jump zoelum
            label zoedog:
                show zoe neutral with d
                zo "Would you like to do this one outside? It’ll make it feel fierce and primal while you rut my backside."
                mc "Suppose we could. The fresh air will stave off the sweat."
                scene bg forestnight with d
                "The two of us take a few steps out into the forest clearing of her cottage and she goes prone down in a patch of grass."
                play music sex1 fadein 3.0
                show zoeb doggystyle
                show zoe doggystyle1
                with d
                mc "Has anyone told you that your ass is sublime?"
                zo "Considering your equally appreciable cock, you can take my ass anytime."
                mc "Hah, you used my own words to rhyme. I wonder when this gimmick will get old."
                "As I get into position before her presented rear, she exudes a high level of excitement, her tail swishes so fervently it keeps brushing against me."
                "The sweet flowery aroma that attracted me here combined with the smell of sex heightens my need to pound her pussy, almost to a beguiling degree."
                play sound cum
                show zoe doggystylev1 with d
                "Her drippy pussy is clearly wet and ready, so I skip teasing and begin the session by pressing aligning the tip of my cock against her pussy and pushing inside."
                "Immediately I sink into the pleasant warmth of her depths, her lips parting bit by bit as it easily accepts me to the hilt in a single smooth motion."
                zo "Ahhhh, ahh… I’m so appreciative that you were present, because that feels extremely pleasant."
                play ambience sex fadein 3.0
                "Her hips twitch as I pull back and sink back in, beginning to rut her at a pleasureful pace for the both of us."
                "Zoe was so wet from the start, she was clearly anticipating this and prepared for it. So it’s not too surprising that she accepted me even if I perhaps wasn’t quite what she wanted."
                "The lustful wetness does allow me to pound her as fast as I want though, choosing to alternate between fast thrusting and then slowing myself down as to pace myself."
                "Each movement causes friction against her swollen clit, and deep sensitive spots within her pussy, filling the zebra girl with bliss."
                zo "Aaahhh, haaahhh, that’s it, I want you to fill me with your seed."
                "Hm, she didn’t rhyme that time. I clearly have my priorities wrong if I’m thinking about that right now, but this zebra girl is an enigma to me on so many levels."
                show zoe doggystylev2 with d
                zo "Aahhahah, yesss... That’s good, keep going at that speed!"
                "Oh, there’s the rhyme! I thrust into my lover at the requested pace, rocking her back and forth against the grass while her toes curl and thighs quiver."
                "Doesn’t seem like it’ll take long for her to reach an orgasm, and indeed she does achieve one far before my own as the mare squeals happily."
                "Her moans grow in lustful intensity, that coupled with the wet schlicking of her pussy, it's pretty much the only thing I can hear as we rut in the dark woods."
                "After her first orgasm, almost impatiently, I feel her own hips begin to rise and fall on my cock. Matching my own pace with some immediacy, and then outmatching it as she speeds up."
                "Her hip movements make her sexual experience immediately clear; she’s done toying around with me, and now she’s going to make me cum."
                "I grab her hips and commit to the accelerating pace, adding a third sound of our bodies slapping together to the mix."
                zo "Ahh, such a sly dog, ahh ahhhh… You’re certainly not a shy lover."
                "My cock begins to twitch and get tighter as my impending orgasm draws closer and closer."
                zo "Now, cum in me I want it all…"
                "At a certain point my orgasm is all but confirmed, but it still takes a few seconds to escape. I use that time to push my body as far as it’ll go, fucking as hard as I can, to push to the heights of euphoria."
                play sound cum
                show zoe doggystylev3 with cum
                play sound cum
                show zoe doggystylev3 with cum
                "And then in one moment of intense bliss, my cock releases its load deep into the waiting mare."
                play sound cum
                show zoe doggystylev3 with cum
                play sound cum
                show zoe doggystylev3 with cum
                zo "Ahh, yess, that’s it… Fill up my womb, until there’s simply no room!"
                stop ambience fadeout 3.0
                stop music fadeout 3.0
                show zoe doggystylecum with d
                "With one final load of cum, I finally empty my balls in the zebra and she slumps onto the grass, panting."
                "I follow her example, lying beside her and resting my head on her voluptuous breasts."
                scene bg black with d
                "After the two of us catch our breathes in the cool outside air for a few moments, we return inside and spend the evening together."
                "In the morning, I return home bright and early."
                $ zoedog = 1
                jump altmorning
            label zoelum:
                zo "Simply splendid, let us begin immediately."
                show bg honeycrispbed
                play music sex1 fadein 3.0
                show zoeb lum
                show zoe lum1
                with d
                "Taking me to her bed, she lays down on her side and soon her legs are spread. Her pussy dripping with anticipation as she presents herself to me."
                zo "I have something that needs to be attended… See how wet my pussy is?  It must be amended."
                "I’d be lying if I said my attention wasn’t immediately drawn to her pussy."
                mc "This promises to be good. Jiggle that ass for me."
                "One of her hands even spreads her ass slightly, wiggling back on forth on my command, and giving me a great view of her genitals."
                "Her pillowy assets really are on full display in this position, allowing my cock to readily come to attention as I stroke it."
                "Zoe looks back at me and grins, anticipating my large cock as I approach and get into position between her legs."
                "Like many denizens of Arcadia, she’s horny as heck and ready for a pounding. Almost with obedience she eyes up my cock eagerly as I begin to poke and prod it against her puffy labia."
                if zoelum == 0:
                    show zoe lum2 with d
                    zo "Hahh… Such a delicious looking cock. I can’t believe my luck having stumbled upon you in the forest while you were on a walk."
                    mc "We’re both lucky. I get to fuck a gorgeous Zebra girl, and you get one of the best fucks in the city."
                    show zoe lum1 with d
                    zo "Phew, and you’re not all talk either… I can’t contest your words, you may be just as good as a wolf man, if not a little bit better."
                    mc "Heh, sounds like I still have something to prove."
                    show zoe lum2 with d
                    "She blushes slightly and returns her gaze to my cock, seemingly impatient and needy as she uses her hand to spread her lips slightly."
                    zo "Actions, my boy."
                else:
                    show zoe lum2 with d
                    zo "Haahh… I always get slightly uncharacteristically giddy in anticipation of sex with you, [playername]…"
                "She blushes slightly and returns her gaze to my cock, seemingly impatient and needy as she uses her hand to spread her lips slightly."
                play sound cum
                show zoe lum3 with d
                play ambience sex fadein 3.0
                "I align and push my shaft against her nether lips, slipping into her wetness and parting her pussy with ease, as I sink into the warmth."
                "Her pussy sucks me inside with ease, her grool coating my entire cock and easily lubricates the tightness of her squeezing walls."
                "As I hold onto her thigh, this position allows me to slide to her absolute depths with ease."
                "And as I pull outwards, I’m able to do long, satisfying, deep thrusts which not only pleasure each inch of my cock, but satisfy her deepest and most sensitive spots."
                zo "Ahhh, aaahhhh! That’s right, slide that cock deep into me, fill us both with joy."
                "Panting and moaning slightly, Zoe caresses and teases her large breasts and erect nipples as I begin to hump her pussy."
                "My deep thrusts gradually pick up pace and her internal squeezing gets more intense, as the pleasure begins to build up within us."
                "With a spare hand entirely free, I find my thumb rubbing her clit intently, while my cock likely creates some friction on her g-spot."
                "The result is a zebra that throws her head back in bliss, and moans loudly. Her thick body mesmerising, as it jiggles back and forth on the bed."
                show zoe lum4 with d
                zo "Gooshh, yess… Keep rubbing my clit, keep rubbing, just like that…"
                "I maintain this exact pace in both my fucking and rubbing, and almost visibly I can see the orgasm building with in my lover."
                "Until finally it erupts, and Zoe begins twitching as her pussy spasms around the base of my cock."
                "Contractions attempt to wring my shaft, although I had paced myself well enough as to not be too close to cumming quite yet."

                if zoelum == 0:
                    "I had something to prove with this girl. I had already planned to give her at least one more orgasm in an attempt to really blow her mind."
                    show zoe lum3 with d
                    zo "Haahhh, y-you’re still going? I’m used to the man cumming by now, haah…"
                    mc "Heh, stubborn further than your eyes can see. I’m no wolf, I’m a man."
                else:
                    show zoe lum3 with d
                    mc "Ready for orgasm two? Don’t lose your mind."

                zo "Come on then big man, show this witch some real magic."
                "Gripping onto her thigh tightly, I start to pump faster into her slick pussy."
                "Her lubricants are so plentiful that I’d barely be able to feel anything if it wasn’t for the incredible tightness of her insides. Tightness that she intentional increases by tensing her muscles."
                "Kneading her own breasts, and tweaking her sensitive nipples, she lavishly indulges in the second assault of intense pleasure as my finger begins to focus on her clit again."
                show zoe lum4 with d
                "Her back arches and teeth grit together as she struggles to hold herself together. Her entire body wriggling and spasming with a lack of control."
                "At this speed and intensity, I could feel my orgasm begin to rise too. My cock grows tight as the familiar urge to unload rises."
                "The pleasure of her insides squeezing my throbbing shaft is really enough to push me straight over the edge."
                "And fortunately, as I finally reach the potent ecstasy of my own powerful orgasm, my lover rolls her eyes and moans out."
                zo "Aahhh, coming! Cum with me!"
                play sound cum
                show zoe lum5 with cum
                play sound cum
                show zoe lum5 with cum
                "The cum was already surging within me, and finally it erupts deeply into Zoe."
                play sound cum
                show zoe lum5 with cum
                play sound cum
                show zoe lum5 with cum
                "Her pussy and womb are filled by an above average load from my cock, all whilst she moans in an orgasmic delight and spurs my last few fatigued thrusts on."
                play sound cum
                show zoe lum6 with d
                stop music fadeout 2.0
                stop ambience fadeout 2.0
                "And as soon as my orgasm dries up, that fatigue finally overwhelms as I sit back limp. Pulling my member out of her with a schlick."
                if zoelum == 0:
                    mc "Phew, how was that?"
                    show zoe lum7 with d
                    zo "Pfft, you were just showing off how good you are in bed."
                    zo "But, that {i}was{/i} tremendous, even compared to a Funris… Maybe… maybe, I have a new favourite instead."
                    mc "Hah, I bet you’d say that to anyone after sex."
                    show zoe lum6 with d
                    zo "Ihihi, I find myself unable to deny such an accusation."
                    zo "If you were trying to impress me because Butters told you to, don’t worry about it."
                    scene bg honeycrispbed with d
                    show zoeb
                    show zoe happy
                    with d
                    zo "I don’t know if her, or your intention was to ‘fuck’ the fetish out of me, but honestly that’d be silly."
                    zo "I told her I’d never turn anyone into a werewolf just to sate my own desires, and that remains true."
                    zo "Not only do ordinary wolf men exist..."
                    zo "But I, like any other mare, just go to the spa, or church when I’m horny. I very rarely practice my fetishes, like most others, I imagine."
                    mc "Is that so? Maybe I’ve misinterpreted what kind of person you are because of your falling out with Butters."
                    show zoe horny with d
                    zo "Mmm… Is that so? If you were going to interpret me as anything, can it be a sexy mommy?"
                    mc "Hm, maybe…"
                    mc "Also, you stopped rhyming."
                    show zoe satisfied with d
                    zo "Because I’m tiiireed, I’ll be asleep in ten minutes… I can’t keep that up all the time."
                    mc "Alright Zoe, let’s snuggle."
                    show zoe horny with d
                    zo "That’s fine with me. After a good nap I shall be able to rhyme."
                else:
                    zo "Phew… That was amazing…"
                    scene bg honeycrispbed with d
                    "Zoe slumps from her side to her back and spreads out like a starfish."
                    "Given her pillowy features, I crawl over her and cuddle."
                    "In an unexpected turn of events however, she rolls on top of me and squashes my face in her breasts."
                    show zoeb
                    show zoe satisfied
                    with d
                    zo "I’ll make you a really good breakfast tomorrow morning. Least I can do for the booty call."
                    mc "*Words muffled in breasts* Sounds good."
                scene bg black with dissolve
                "The two of us snooze while snuggled together."
                "I return home early in the morning."
                $ zoelum = 1
                jump altmorning
        "Sex with Alraune":
            if alraunesex == 0:
                show alraune neutral with d
                alraune "Bleh, you’re totally gonna knock me up if you cum inside… I guess I can live with that."
                alraune "Come on then, let’s go to my room."
                scene bg poyobedroom with d
                "I step into a fairly regular room. This little pet relationship is reminding me of Butters and Poyo a little."
                mc "So, this’ll be a bit of revenge for last time, then."
                show alraune laughing with d
                alraune "Meh, if you must see it that way. I suppose that did come back to bite me in the ass."
                alraune "This is what I get, my punishment for being a little naughty!"
                show alraune horny with d
                alraune "So, I’ll let you do it, fuck me, fill me, and knock me up!"
                "I squint at the Alraune slightly confused, having absolutely no logistical idea of how to actually fuck her, considering there’s a giant plant bulb in the way."
                mc "Okay, I’m just wondering what the best method to go about doing this is…"
                show alraune neutral with d
                alraune "Oh my gosh, is it your first time too?!"
                mc "Uh, no, it’s just… How do I reach your pussy? Even if you were to bend over your leaves are in the way."
                show alraune happy with d
                alraune "Ohhh, hehehe… There’s room for two in this bulb you know… It’s ‘designed’ that way, hehehe…"
            else:
                show alraune neutral with d
                alraune "Again? I guess I did ask!"
                alraune "I dunno what’s come over me lately, but I’m just a total slut lately, heh."
                scene bg poyobedroom with d
                "I step into a fairly regular room. As before there isn’t much here other than basic entertainment and some storage. A plant girl sure doesn’t need much to distract her."
                "And there’s no distraction for Alraune too, as she immediately begins acting sexually."
            show alraune horny with d
            "She leans back slightly and spreads her pussy, her legs although they do separate at the hips seem to be stuck together at the base resulting in an interesting angle."
            "And indeed, she is correct, there’s a noticeable area before her within her flower…"
            "Cautiously, I step closer, pulling aside leaves as I get adjacent to the rose bud."
            alraune "Don’t be shy… The dew feels great!"
            "I dip my finger into the pinkish goop, and not particularly to my surprise, it’s the exact pink aphrodisiac from the cave before."
            "Fortunately, her leaves also relieve the effects of that aphrodisiac, so I forgo caution and begin to lift myself into the bud."
            play music sex1 fadein 3.0
            scene alrauneb sex
            show alraune sex1
            with d
            mc "Aaaahhhh…"
            "Warmth and comfort like a hug consume my body as I step into the pleasant bulb."
            mc "This is really nice… We’re pretty damn close to each other though."
            if alraunesex == 0:
                alraune "Oh fuck, I’m not the only one getting extremely horny, right? Ohh, gosh…"
            else:
                alraune "I think I get it now… When a man steps into my pool it immediately actives some kind of sex instinct, it makes me sooooo hornyyyy."

            "I’m already half erect at this point, and immediately tingles of the aphrodisiac aid in bringing out the other half of that erection."
            "Within a few seconds, my precum dripping erection is pressed against her belly."
            if alraunesex == 0:
                show alraune sex2 with d
                alraune "Hahh, gosh, I think I just started ovulating…"
                mc "Does your species do that around a male?"
                alraune "Mhm… Whenever one steps into my flower, hehe…"
                alraune "I guess that means you’ll have to pollinate me…"
            else:
                show alraune sex2 with d
                alraune "Haahh, gosh, pollinate me with your seed!"
            "She bashfully giggles as she takes my cock and guides it between her legs."
            "With my tip poking at her entrance, I grasp both of her hips and push in."
            if alraunesex == 0:
                show alraune sex1 with d
                mc "This purple liquid really does wonders for an erection, aren’t you always horny?"
                alraune "Me, h-horny? Yessshhh!"
                mc "No, I mean…"
                alraune "Fuck me, fuck me!"
                mc "Oookay, you got it."
            else:
                show alraune sex1 with d
                alraune "Ahh, haaahhh… Ahhhh… This feels far too good… Like… I can’t tell who’s more drunk on arousal, you or me."
            play ambience sex fadein 3.0
            show alraune sex2 with d
            "She leans back as I thrust forward, giving me as much room as possible in this unusual angle of penetration."
            "Despite the Alraune’s large overall body, her feminine frame is petite as I handle her. My hands almost encompassing her entire hips as I tightly grip her for leverage. Her breasts bobbing up and down with the force of each thrust."
            "Her cute breasts, and their function of which I’m not entirely sure, sport two green nipples which had become noticeably puffy and erect since penetration."
            "Tweaking and teasing the nipples results in girlish moans escaping from my lover, as it appears, they’re sensitive like any other girl."
            show alraune sex3 with d
            "And as my hand explores the rest of my lover, I also find my way down to her pussy, teasing around for a clitoris to rub which greatly excites her also."
            "Regarding her pussy, the tightness is naturally immense with her thighs locked together, creating a sensation similar to standing sex."
            "And the purple aphrodisiac enhances the sensation, to such a degree that it probably robs me of free will, and forces me to fuck."
            "Come to think of it, that’s probably how Alraunes ‘catch’ their mates."
            if alraunesex == 0:
                show alraune sex2 with d
                alraune "Ahhhhah, I want you to cum in me lots and lots!"
                mc "Hang on… Am I not just cumming inside you once?!"
                alraune "Nooooo, I want a lot more cummies than that!"
            else:
                show alraune sex2 with d
                alraune "Fill me up with your cummies!"
            "I gulp, and just focus on the fucking, there isn’t a lot I can do since my mind is so beguiled and focused on sex."
            "Her internal juices which completely coat my member allow me to thrust faster, but I soon realize that her internal juices are exactly the same purple liquid that I’m currently stood in."
            "This purple liquid sends pleasureful tingles throughout my cock which travel through my body like a wave of euphoria."
            "All thought without regard to sex leaves my mind, as I pummel her tight green plant pussy. It squeezes and suckles around my cock with an increasing aggression, as if it’s purposely trying to milk me."
            "All of these sensations send me into a spiral of intoxicated pleasure. Overcome with lust, my hips accelerate and I pound the alraune with all my effort."
            "She yelps with surprise, letting out a giggle and then a moan as pleasure also crashes through her. My cock repeatedly pumping into the deepest reaches of her warm flesh."
            show alraune sex3 with d
            alraune "Yesss, yesss, ahhaaahhhh… Fuck me, fuck me!"
            "It doesn’t take too long for a tension in my taint to arise, signalling an impending orgasm."
            alraune "Oh my goshh, aaaaahhh!"
            "Since she doesn’t shut up moaning, I temporarily press my thumb into her mouth to suckle on, which she gratefully does."
            "Ironically, this action only seems to excite her more as her entire body quivers with orgasmic bliss, the very leaves and petals of the flower trembling with pleasure."
            "And with her orgasm, mine isn’t too far off either. Her slick pussy squeezes one last time and triumphantly it almost immediately pushes me over the edge as my cock swells and prepares to unload."
            "Trembling, my member releases a hot load of cum directly into her pussy."
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            "The release is powerful enough to send shivers down my spine, as a truly inhuman amount of jizz pours out of me and fills my lover up to the brim."
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            play sound cum
            show alraune sex4 with fcum
            stop ambience fadeout 3.0
            stop music fadeout 15.0
            "Even when my orgasm dissipates however, the positioning keeps my cock lodged deep inside her, and the aphrodisiac keeps me very much erect."
            "Despite that, for the briefest moment my mind is clear. Taking some initiative, I pinch off a tiny bit of her leaf and nibble it to quell the overwhelming effects of the purple goo."
            if alraunesex == 0:
                show alraune sex6 with d
                alraune "Owww! What was that for? Bully!"
                mc "Mmph? *Munch* Sorry, I didn’t realize that’d hurt you."
            else:
                show alraune sex6 with d
                alraune "Eep, easy on the leaves…"
                mc "I wonder how fast these things grow… Like, could you run out?"
                alraune "Nahh, all my body parts grow back, eventually."
                alraune "Although if my brain is damaged and regrown, I could be a completely different person! Weird, right?"
                mc "Is that true? I guess I’ll take your word for it."
            show alraune sex5 with d
            "Almost immediately, the aphrodisiac seems to wear off, and my cock returns to the state you’d expect after an orgasm: soft and sensitive."
            scene bg poyobedroom with d
            "And with that, I take the opportunity to slip out of the Alraune’s sex trap. The purple liquid treating me like I’m hydrophobic, and not coming with me, leaving me completely dry as I step out."
            if alraunesex == 0:
                show alraune neutral with d
                alraune "Ohh man… But I’m still so horny! You’re such a dick!"
                alraune "And there’s no way you got me pregnant after one time…"
                alraune "You’re going to have to fuck me lots and lots! Okay?"
                mc "Yeah, yeah… I just didn’t want you to put me in a coma."
                show alraune horny with d
                alraune "Pfft, I couldn’t even have sex with you without your consent anyway. With my body, there’s almost no natural position where I can be on top. All I can do is use my feeder, and that’s no fun…"
                mc "Yeah, and that’s exactly why you have the aphrodisiac to trick men into taking the initiative."
                mc "I won’t fall for your trick this time. But I might have sex with you again in the future, that was exceedingly pleasureful."
                show alraune laughing with d
                alraune "Oh, you will? That’d really make my day!"
                show alraune neutral with d
                alraune "Oh, and in the morning, can you give me some cum for breakfast? I’d love that!"
                mc "Damn, you’re so needy when it comes to my cum. But I don't think I'll be sticking around for that long."
                show alraune happy with d
                alraune "Least I tried! That’s a monster girl for you! Hehe."
            else:
                show alraune neutral with d
                alraune "Hmm… It seems that as soon as you step out of my plant, that sex instinct fades pretty quickly… I can breathe easy with that knowledge."
                show alraune happy with d
                alraune "You’re pretty sly nibbling on some leaf between orgasms."
                alraune "Most men would be far too focused on sex to do that."
                mc "What can I say, my aversion to death is greater than my need for sex."
                show alraune laughing with d
                alraune "Hehe, as if I would hurt you!"
            $ alraunesex = 1
            scene bg black with d
            "The two of us eventually settle down, but she doesn’t have a bed because she just sleeps in her flower."
            "So I end up going back home to sleep."
            jump sleep
        "Back":
            jump worldmap
