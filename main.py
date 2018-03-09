from flask import Flask, render_template, request
from image import Search
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/searchImage', methods=['POST', 'GET'])
def searchImages():
    def adj_n(words):
        words = {'adj': filterWord(words['adj']), 'n': filterWord(words['n'])}
        lines = [
            ("You won't believe what this " + words['adj'] + " " + words['n'] + " does next!!!", words['adj'] + " " + words['n']),
            ("This " + words['adj'] + " " + words['n'] + " will make you laugh until you cry!", words['adj'] + " " + words['n'] + " laugh"),
			(words['adj'] + " " + words['n'] + " are Illegal?? Find out Why", words['adj'] + " " + words['n']),
			("Check out how " + words['adj'] + " " + words['n'] + " have changed for the better in 2018!!", words['adj'] + " " + words['n'])
		]
        return lines

    def adv_v(words):
        words = {'adv': filterWord(words['adv']), 'v': filterWord(words['v'])}
        lines = [
			("The best way to " + words['adv'] + " " + words['v'] + " this holiday season", words['adv'] + " " + words['v']),
			("The fastest way to " + words['adv'] + " " + words['v'] + " without your parents finding out!", words['adv'] + " " + words['v'])
        ]
        return lines
    def adj1_n1_n2_adj2(words):
        words = {'adj1': filterWord(words['adj1']), 'n1': filterWord(words['n1']), 'adj2': filterWord(words['adj2']), 'n2': filterWord(words['n2'])}
        lines = [
            ("You won't believe what this " + words['adj1'] + " " + words['n1'] + " did to this " + words['adj2'] + " " + words['n2'], words['n1'] + " " + words['adj2'] + " " + words['n2']),
            ("What this " + words['adj1'] + " " + words['n1'] + " did for this " + words['adj2'] + " " + words['n2'] + "... Amazing!", "amazing " + words['n1'] + " " + words['n2'])
		]
        return lines
    def v_n(words):
        words = {'v': filterWord(words['v']), 'n': filterWord(words['n'])}
        lines = [
            ("How to " + words['v'] + " your " + words['n'], words['v'] + " " + words['n']),
            ("You should never " + words['v'] + " this kind of " + words['n'], words['v'] + " " + words['n']),
        ]
        return lines
    def ving_n(words):
        words = {'ving': filterWord(words['ving']), 'n': filterWord(words['n'])}
        lines = [
            ("Donald Trump is " + words['ving'] + " " + words['n'], words['ving'] + " " + words['n']),
            ("Did you know you could make money by " + words['ving'] + " " + words['n'], "money " + words['ving'] + " " + words['n'])
        ]
        return lines
    formTypes = {
        "adj_n": adj_n,
        "adj1_n1_n2_adj2": adj1_n1_n2_adj2,
        "adv_v": adv_v,
        "v_n": v_n,
        "ving_n": ving_n
    }
    if request.method == 'POST':
        words = request.form
        print words
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
