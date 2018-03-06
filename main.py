from flask import Flask, render_template, request
from image import Search
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/searchImage', methods=['POST', 'GET'])
def searchImages():
    def adj_noun(words):
        words = {'adj': filterWord(words['adj']), 'noun': filterWord(words['noun'])}
        lines = [
            ("You won't believe what this " + words['adj'] + " " + words['noun'] + " does next!!!", words['adj'] + " " + words['noun']),
            ("This " + words['adj'] + " " + words['noun'] + " will make you laugh", words['adj'] + " " + words['noun'] + " laugh")
        ]
        return lines
<<<<<<< Updated upstream
    def adv_noun(words):
=======
    def adv_v(words):
        words = {'adv': filterWord(words['adv']), 'v': filterWord(words['v'])}
>>>>>>> Stashed changes
        lines = [
            ("how to " + words['adv'] + " your " + words['noun'], words['adv'] + " " + words['noun']),
            ("Donald Trump is " + words['adv'] + words['noun'], words['adv'] + " " + words['noun'])
        ]
        return lines
    formTypes = {
        "adj_noun": adj_noun,
        "adv_noun": adv_noun
    }
    if request.method == 'POST':
        words = request.form
        clickbaitTitle, query = random.choice(formTypes["_".join([key for key, value in words.iteritems()])](words))
        search = (Search(5).getThumbs(query))

        return render_template("answer.html", title = clickbaitTitle, items=search)

def filterWord(word):
    badWords = ['2g1c', 'acrotomophilia', 'anal', 'anilingus', 'anus', 'apeshit', 'arsehole', 'ass', 'asshole', 'assmunch', 'autoerotic', 'babeland', 'bangbros', 'bareback', 'barenaked', 'bastard', 'bastardo', 'bastinado', 'bbw', 'bdsm', 'beaner', 'beaners', 'bestiality', 'bimbos', 'birdlock', 'bitch', 'bitches', 'blowjob', 'blumpkin', 'bollocks', 'bondage', 'boner', 'boob', 'boobs', 'bukkake', 'bulldyke', 'bullshit', 'bunghole', 'busty', 'butt', 'buttcheeks', 'butthole', 'camgirl', 'camslut', 'camwhore', 'carpetmuncher', 'circlejerk', 'clit', 'clitoris', 'clusterfuck', 'cock', 'cocks', 'coprolagnia', 'coprophilia', 'cornhole', 'coon', 'coons', 'creampie', 'cum', 'cumming', 'cunnilingus', 'cunt', 'darkie', 'daterape', 'deepthroat', 'dendrophilia', 'dick', 'dildo', 'dingleberry', 'dingleberries', 'doggiestyle', 'doggystyle', 'dolcett', 'domination', 'dominatrix', 'dommes', 'dvda', 'ecchi', 'ejaculation', 'erotic', 'erotism', 'escort', 'eunuch', 'faggot', 'fecal', 'felch', 'fellatio', 'feltch', 'femdom', 'figging', 'fingerbang', 'fingering', 'fisting', 'footjob', 'frotting', 'fuck', 'fuckin', 'fucking', 'fucktards', 'fudgepacker', 'futanari', 'genitals', 'goatcx', 'goatse', 'gokkun', 'goodpoop', 'goregasm', 'grope', 'g-spot', 'guro', 'handjob', 'hardcore', 'hentai', 'homoerotic', 'honkey', 'hooker', 'humping', 'incest', 'intercourse', 'jailbait', 'jigaboo', 'jiggaboo', 'jiggerboo', 'jizz', 'juggs', 'kike', 'kinbaku', 'kinkster', 'kinky', 'knobbing', 'lolita', 'lovemaking', 'masturbate', 'milf', 'motherfucker', 'muffdiving', 'nambla', 'nawashi', 'negro', 'neonazi', 'nigga', 'nigger', 'nimphomania', 'nipple', 'nipples', 'nude', 'nudity', 'nympho', 'nymphomania', 'octopussy', 'omorashi', 'orgasm', 'orgy', 'paedophile', 'paki', 'panties', 'panty', 'pedobear', 'pedophile', 'pegging', 'penis', 'pissing', 'pisspig', 'playboy', 'ponyplay', 'poof', 'poon', 'poontang', 'punany', 'poopchute', 'porn', 'porno', 'pornography', 'pthc', 'pubes', 'pussy', 'queaf', 'queef', 'quim', 'raghead', 'rape', 'raping', 'rapist', 'rectum', 'rimjob', 'rimming', 'sadism', 'santorum', 'scat', 'schlong', 'scissoring', 'semen', 'sex', 'sexo', 'sexy', 'shemale', 'shibari', 'shit', 'shitblimp', 'shitty', 'shota', 'shrimping', 'skeet', 'slanteye', 'slut', 's&m', 'smut', 'snatch', 'snowballing', 'sodomize', 'sodomy', 'spic', 'splooge', 'spooge', 'spunk', 'strapon', 'strappado', 'suck', 'sucks', 'swastika', 'swinger', 'threesome', 'throating', 'tit', 'tits', 'titties', 'titty', 'topless', 'tosser', 'towelhead', 'tranny', 'tribadism', 'tubgirl', 'tushy', 'twat', 'twink', 'twinkie', 'undressing', 'upskirt', 'urophilia', 'vagina', 'vibrator', 'vorarephilia', 'voyeur', 'vulva', 'wank', 'wetback', 'xx', 'xxx', 'yaoi', 'yiffy', 'zoophilia']

    for badWord in badWords:
        if word == badWord:
            return "@!%$*"
    return str(word)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
