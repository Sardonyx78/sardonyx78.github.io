# I made this script so I wouldnt need to do the skills one by one

fh = open("generated.js", "w")

skillsLeft = {
    'lua': {
        'colors': {
            'background': "#B4CDEB",
            'front': "#4E70E9"
        },
        'percent': "54.89650528106613%"
    },
    'react': {
        'colors': {
            'background': "#C1F6FF",
            'front': "#00D8FF"
        },
        'percent': "68.37917345998441%"
    },
    'html': {
        'colors': {
            'background': "#FDC4B5",
            'front': "#DD4B25"
        },
        'percent': "89.56723612391012%"
    },
    'css': {
        'colors': {
            'background': "#C6D1FF",
            'front': "#254BDD"
        },
        'percent': "74.63847735166938%"
    }
}

skillsRight = {
    'js': {
        'colors': {
            'background': "#FFE8AD",
            'front': "#F9B300"
        },
        'percent': "81.38158361097328%"
    },
    'ts': {
        'colors': {
            'background': "#B5D0EE",
            'front': "#3178C6"
        },
        'percent': "81.38158361097328%"
    },
    'node': {
        'colors': {
            'background': "#D7EFBD",
            'front': "#8BC74B"
        },
        'percent': "81.38158361097328%"
    },
    'java': {
        'colors': {
            'background': "#BDD5E4",
            'front': "#52819F"
        },
        'percent': "48.15517119160701%"
    }
}

outRight = ""
outLeft = ""

for key in skillsRight:
    skill = skillsRight[key]
    outRight = outRight + '<div class="skill ' + key + '" style="background: ' + skill['colors']['background'] + '"><img draggable="false" src="assets/' + key + '.png" alt="' + key + \
        '"><div class="skillbar" style="width: ' + \
        skill['percent'] + '"><div class="skillbarfill" style="background: ' + \
        skill['colors']['front'] + '"></div></div></div>'

for key in skillsLeft:
    skill = skillsLeft[key]
    outLeft = outLeft + '<div class="skill ' + key + '" style="background: ' + skill['colors']['background'] + '"><img draggable="false" src="assets/' + key + '.png" alt="' + key + \
        '"><div class="skillbar" style="width: ' + \
        skill['percent'] + '"><div class="skillbarfill" style="background: ' + \
        skill['colors']['front'] + '"></div></div></div>'


# Thank you ES gods for this unneccessary feature
fh.write("skillsLeft.innerHTML = '" + outLeft +
         "'; skillsRight.innerHTML = '" + outRight + "'")
