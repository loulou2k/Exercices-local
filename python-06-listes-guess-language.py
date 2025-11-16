# Exercice 6.3 Recherche de langue
import string

ENGLISH = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]

FRENCH = [8.173, 0.901, 3.345, 3.669, 16.734, 1.066, 0.866, 0.737, 7.579, 0.613, 0.049, 5.456, 2.968, 7.095, 5.819, 2.521, 1.362, 6.693, 7.948, 7.244, 6.429, 1.838, 0.074, 0.427, 0.128, 0.326]

GERMAN = [ 7.094, 1.886, 2.732, 5.076, 16.396, 1.656, 3.009, 4.577, 6.550, 0.268, 1.417, 3.437, 2.534, 9.776, 3.037, 0.670, 0.018, 7.003, 7.577, 6.154, 5.161, 0.846, 1.921, 0.034, 0.039, 1.134	]

SPANISH = [ 12.027, 2.215, 4.019, 5.010, 12.614, 0.692, 1.768, 0.703, 6.972, 0.493, 0.011, 4.967, 3.157, 7.023, 9.510, 2.510, 0.877, 6.871, 7.977, 4.632, 3.107, 1.138, 0.017, 0.215, 1.008, 0.467]

LANGS = [ENGLISH, FRENCH, GERMAN, SPANISH]

TRTAB = str.maketrans(
    "àâäçèéêëìíîïñòóôõöùúûüýÿšž",
    "aaaceeeeiiiinooooouuuuyysz"
)

LCELR = """
MaÃ®tre Corbeau, sur un arbre perchÃ©,
           Tenait en son bec un fromage.
       MaÃ®tre Renard, par l'odeur allÃ©chÃ©,
           Lui tint Ã  peu prÃ¨s ce langage :
       Et bonjour, Monsieur du Corbeau,
    Que vous Ãªtes joli ! que vous me semblez beau !
           Sans mentir, si votre ramage
           Se rapporte Ã  votre plumage,
     Vous Ãªtes le PhÃ©nix des hÃ´tes de ces bois.
Ã€ ces mots le Corbeau ne se sent pas de joie,
           Et pour montrer sa belle voix,
   Il ouvre un large bec, laisse tomber sa proie.
   Le Renard s'en saisit, et dit : Mon bon Monsieur,
              Apprenez que tout flatteur
     Vit aux dÃ©pens de celui qui l'Ã©coute.
   Cette leÃ§on vaut bien un fromage sans doute.
           Le Corbeau honteux et confus
   Jura, mais un peu tard, qu'on ne l'y prendrait plus.
"""

IF = """
If you can keep your head when all about you   
    Are losing theirs and blaming it on you,   
If you can trust yourself when all men doubt you,
    But make allowance for their doubting too;   
If you can wait and not be tired by waiting,
    Or being lied about, donâ€™t deal in lies,
Or being hated, donâ€™t give way to hating,
    And yet donâ€™t look too good, nor talk too wise:

If you can dreamâ€”and not make dreams your master;   
    If you can thinkâ€”and not make thoughts your aim;   
If you can meet with Triumph and Disaster
    And treat those two impostors just the same;   
If you can bear to hear the truth youâ€™ve spoken
    Twisted by knaves to make a trap for fools,
Or watch the things you gave your life to, broken,
    And stoop and build â€™em up with worn-out tools:

If you can make one heap of all your winnings
    And risk it on one turn of pitch-and-toss,
And lose, and start again at your beginnings
    And never breathe a word about your loss;
If you can force your heart and nerve and sinew
    To serve your turn long after they are gone,   
And so hold on when there is nothing in you
    Except the Will which says to them: â€˜Hold on!â€™

If you can talk with crowds and keep your virtue,   
    Or walk with Kingsâ€”nor lose the common touch,
If neither foes nor loving friends can hurt you,
    If all men count with you, but none too much;
If you can fill the unforgiving minute
    With sixty secondsâ€™ worth of distance run,   
Yours is the Earth and everything thatâ€™s in it,   
    Andâ€”which is moreâ€”youâ€™ll be a Man, my son!
"""

POEMAXX = """
Puedo escribir los versos mÃ¡s tristes esta noche.

Escribir, por ejemplo: â€œLa noche estÃ¡ estrellada,
y tiritan, azules, los astros, a lo lejos.â€

El viento de la noche gira en el cielo y canta.

Puedo escribir los versos mÃ¡s tristes esta noche.
Yo la quise, y a veces ella tambiÃ©n me quiso.

En las noches como Ã©sta la tuve entre mis brazos.
La besÃ© tantas veces bajo el cielo infinito.

Ella me quiso, a veces yo tambiÃ©n la querÃ­a.
CÃ³mo no haber amado sus grandes ojos fijos.

Puedo escribir los versos mÃ¡s tristes esta noche.
Pensar que no la tengo. Sentir que la he perdido.

Oir la noche inmensa, mÃ¡s inmensa sin ella.
Y el verso cae al alma como al pasto el rocÃ­o.

QuÃ© importa que mi amor no pudiera guardarla.
La noche estÃ¡ estrellada y ella no estÃ¡ conmigo.

Eso es todo. A lo lejos alguien canta. A lo lejos.
Mi alma no se contenta con haberla perdido.

Como para acercarla mi mirada la busca.
Mi corazÃ³n la busca, y ella no estÃ¡ conmigo.

La misma noche que hace blanquear los mismos Ã¡rboles.
Nosotros, los de entonces, ya no somos los mismos.

Ya no la quiero, es cierto, pero cuÃ¡nto la quise.
Mi voz buscaba el viento para tocar su oÃ­do.

De otro. SerÃ¡ de otro. Como antes de mis besos.
Su voz, su cuerpo claro. Sus ojos infinitos.

Ya no la quiero, es cierto, pero tal vez la quiero.
Es tan corto el amor, y es tan largo el olvido.

Porque en noches como Ã©sta la tuve entre mis brazos,
mi alma no se contenta con haberla perdido.

Aunque Ã©ste sea el ultimo dolor que ella me causa,
y estos sean los Ãºltimos versos que yo le escribo.
"""

GOETHE = """
Wer reitet so spÃ¤t durch Nacht und Wind?
Es ist der Vater mit seinem Kind;
Er hat den Knaben wohl in dem Arm,
Er faÃŸt ihn sicher, er hÃ¤lt ihn warm.

Mein Sohn, was birgst du so bang dein Gesicht? -
Siehst Vater, du den ErlkÃ¶nig nicht?
Den ErlenkÃ¶nig mit Kron und Schweif? -
Mein Sohn, es ist ein Nebelstreif. -

Â»Du liebes Kind, komm, geh mit mir!
Gar schÃ¶ne Spiele spiel ich mit dir;
Manch bunte Blumen sind an dem Strand,
Meine Mutter hat manch gÃ¼lden Gewand.Â«

Mein Vater, mein Vater, und hÃ¶rest du nicht,
Was ErlenkÃ¶nig mir leise verspricht? -
Sei ruhig, bleibe ruhig, mein Kind;
In dÃ¼rren BlÃ¤ttern sÃ¤uselt der Wind. -

Â»Willst, feiner Knabe, du mit mir gehn?
Meine TÃ¶chter sollen dich warten schÃ¶n;
Meine TÃ¶chter fÃ¼hren den nÃ¤chtlichen Reihn
Und wiegen und tanzen und singen dich ein.Â«

Mein Vater, mein Vater, und siehst du nicht dort
ErlkÃ¶nigs TÃ¶chter am dÃ¼stern Ort? -
Mein Sohn, mein Sohn, ich seh es genau:
Es scheinen die alten Weiden so grau. -

Â»Ich liebe dich, mich reizt deine schÃ¶ne Gestalt;
Und bist du nicht willig, so brauch ich Gewalt.Â«
Mein Vater, mein Vater, jetzt faÃŸt er mich an!
ErlkÃ¶nig hat mir ein Leids getan! -

Dem Vater grauset's, er reitet geschwind,
Er hÃ¤lt in den Armen das Ã¤chzende Kind,
Erreicht den Hof mit MÃ¼he und Not;
In seinen Armen das Kind war tot.
"""

def guess_language(text):
    """
    Estimation du langage utilisÃ© dans la chaine de caractÃ¨res passÃ©e en 
    argument par analyse de frÃ©quence

    Args:
        text: chaine de caractÃ¨res

    Returns:
        'english', 'french', 'german' or 'spanish'
        
    >>> guess_language("aaaaaaaabcccddddeeeeeeeeeeeeeffgghhhhhhiiiiiiikllllmmnnnnnnnoooooooopprrrrrrsssssstttttttttuuuvwwyy")
    'english'
    >>> guess_language("aaaaaaaaaaaabbccccdddddeeeeeeeeeeeeefgghiiiiiiilllllmmmnnnnnnnoooooooooopppqrrrrrrrsssssssstttttuuuvy")
    'spanish'
    >>> guess_language("aaaaaaabbcccdddddeeeeeeeeeeeeeeeeffggghhhhhiiiiiiiklllmmmnnnnnnnnnnoooprrrrrrrssssssssttttttuuuuuvwwz")
    'german'
    >>> guess_language("aaaaaaaabcccddddeeeeeeeeeeeeeeeeefghiiiiiiiijlllllmmmnnnnnnnoooooopppqrrrrrrrsssssssstttttttuuuuuuvv")
    'french'
    """
    # transform text to lowercase
    # remove accented characters with translation table TRTAB
    # use string.ascii_lowercase to compute letter frequencies. Length matters !   
    # compute least squares differences with the 4 reference tables
    # search for min
    # select and return language accordingly

    freq = []
    text = text.lower().translate(TRTAB)
    total = 0
    for c in string.ascii_lowercase:
        count = text.count(c)
        freq.append(count)
        total += count

    if total == 0:
        return None

    freq = [f * 100.0 / total for f in freq]

    diffs = []
    for ref in LANGS:
        diff = sum((f - r) ** 2 for f, r in zip(freq, ref))
        diffs.append(diff)

    idx_min = diffs.index(min(diffs))
    languages = ['english', 'french', 'german', 'spanish']

    return languages[idx_min]

print(guess_language(LCELR))   
print(guess_language(IF))      
print(guess_language(GOETHE))  
print(guess_language(POEMAXX)) 
