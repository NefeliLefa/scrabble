from classes import Game
g=Game("greek7.txt")

def guidelines():
    '''
    SCRABBLE 
    
    ΚΛΑΣΕΙΣ
    
    SaKClass:
    Κλάση που ετοιμάζει το σακουλάκι του παιχνιδιού.
    __init__(): Κατασκευαστής της κλάσης, που δημιουργεί το σακουλάκι self.bag ως μια κενή λίστα και καλεί την prepare().

    prepare(): Δημιουργεί ένα λεξικό που έχει ως κλειδί ένα γράμμα και ως τιμή την αξία του γράμματος στο scrabble. Έτσι, κάθε γράμμα μέσα στο λεξικό, έχει ως δείκτη 
    έναν φυσικό αριθμό. 

    getletter(): Με βάση τους προαναφερθέντες δείκτες θα γίνεται και η τυχαία επιλογή γραμμάτων για κάθε παίκτη, μέσω 
    της συνάρτησης randint. 

    getletters(): Αν το σακουλάκι έχει λιγότερα γράμματα από αυτά που δικαιούται ο παίκτης, τότε ο παίκτης παίρνει όλα τα γράμματα που έχει το σακουλάκι, αλλιώς παίρνω 
    ν=numbrofletters γραμματα.

    putbackletters(): Επιστρέφονται γράμματα στο σακουλάκι, ενώνοντας ουσιαστικά δυο λίστες. Η μία είναι τα γράμματα που είναι στο σακουλάκι και η άλλη η λίστα των γραμμάτων που 
    θέλουμε να επιστραφούν.

    getnumberofletters(): Παίρνουμε το πόσα γράμματα έχουν μείνει στο σακουλάκι μέσω του μήκους (len).
    
    __repr__(): Δείχνει πόσα γράμματα μένουν στο σακουλάκι καλώντας την getnumberofletters().

    Language:
    Κλάση που φτιάχνει το λεξικό που θα χρησιμοποιηθεί για το παιχνίδι. 
    __init__(): Κατασκευαστής της κλάσης. Η παράμετρος filename περνά στην ιδιότητα self.filename και δημιουργείται ένα κενό λεξικό self.dictionary και καλεί την read_words 
    για να διαβάσει το αρχείο filename.txt .

    read_words: Διαβάζει τις λέξεις του αρχείου .txt και δημιουργεί ένα λεξικό που έχει ως κλειδιά τα γράμματα του αλφάβητου και ως τιμές λίστες με όλες τις λέξεις 
    που αρχίζουν από αυτό το γράμμα. 
    
    elegxos_lexis: Ελέγχει αν μια λέξη ανήκει στο λεξικό. Αρχικά ψάχνει αν το πρώτο γράμμα της λέξης ανήκει στα κλειδιά του λεξικού, και αν ναι ψάχνει στην τιμή-λίστα
    του λεξικού, αν υπάρχει η λέξη.

    Player:
    Βασική κλάση (υπερκλάση) των Human & Computer. 

    __init__:Δίνει το όνομα Pc στον υπολογιστη και δημιουργεί ιδιότητα που θα ζητάει όνομα από τον άνθρωπο-παίκτη. Ορίζει τους πόντους αρχικά να είναι 0, οι κινήσεις να είναι 0
    και δημιουργεί μια κενή λίστα, η οποία θα είναι τα γράμματα που θα έχουν οι παίκτες σε κάθε γύρο.
    
    giveletters: Δίνει γράμματα στους παίκτες ενώνοντας δύο λίστες. 

    passturn: Καλύπτει την περίπτωση που ένας παίκτης πάει πάσο. Δημιουργεί αρχικά μια κενή λίστα στην οποία προστίθονται τα γράμματα του παίκτη. Έπειτα, αδειάζει η λίστα του
    παίκτη, τα γράμματά του επιστρέφονται στο σακουλάκι, καλώντας την putbackletters για την προσωρινή λίστα. Ύστερα, καλείται η getletters για να πάρουμε 7 καινούργια γράμματα
    από το σακουλάκι και τα δίνουμε στον παίκτη μέσω της giveletters. Πάσο μπορεί να πάει και ο άνθρωπος και ο υπολογιστής.
    
    number_of_letters(): Επιστρέφει πόσα γράμματα έχει ο κάθε παίκτης μετρώντας το μήκος της λίστας του.

    get_letters_display(): Παρουσιάζει τα γράμματα με την αξία του κάθε γράμματος από δίπλα. 
    
    display_points(): Δείχνει τους πόντους που έχει ο κάθε παίκτης. 

    __repr__(): Παρουσιάζεται πριν παίξει ο κάθε παίκτης και του δείχνει τι γράμματα έχει.
    
    get_all_posible_words(): Βρίσκει κάθε πιθανή λέξη κάνοντας μεταθέσεις στα γράμματα και έπειτα ελέγχει για κάθε λέξη αν ανήκει στο λεξικό.

    get_best_word(): Υπολογίζει τους πόντους που πιάνει κάθε λέξη και διαλέγουμε αυτήν με τους περισσότερους. 

    Human:
    Παράγωγη κλάση του Player. 
    
    play(): Περιγράφει το πώς παίζει ο άνθρωπος, ελέγχει αν η λέξη που δίνει είναι σωστή. Συγκεκριμένα αν μπορεί να γραφεί με τα γράμματα που έχει ο παίκτης και αν 
    ανήκει στο λεξικό. Έπειτα υπολογίζει τους πόντους της. 
    
    teach(): Mαθαίνει στον παίκτη ποιά είναι η καλύτερη λέξη που θα μπορούσε να είχε γράψει με τα γράμματα που έχει και πόσους πόντους θα έπιανε.

    Computer:
    Παράγωγη κλάση του Player. 
    
    play(): Περιγράφει το πώς παίζει ο υπολογιστής χρησιμοποιώντας κυρίως συναρτήσεις της υπερκλάσης Player. Αν η final_choice που έχει επιστραφεί από την get_best_word 
    είναι κενό, τότε ο υπολογιστής πάει πάσο.

    Game:
    Κλάση διαμεσολαβητή μεταξύ των κλάσεων, που περιγράφει το πώς εξελίσσεται μια παρτίδα. 

    setup(): Στην αρχή ο χρήστης καλείται να διαλέξει αν θέλει να δει τα προηγούμενα σκορ, αν θέλει να μεταβεί στις ρυθμίσεις, αν θέλει να παίξει ή αν θέλει να βγει από το παιχνίδι. 
    Αν επιλέξει 1: Αν δεν υπάρχουν προηγούμενα παιχνίδια, εμφανίζεται αντίστοιχο μήνυμα. Αν υπάρχουν, δηλαδή υπάρχει αρχείο SCORES, διαβάζονται τα δεδομένα. 
    Σε κάθε περίπτωση, μετά επιστρέφει στο κεντρικό μενού.
    Αν επιλέξει 2: Μετάβαση στις ρυθμίσεις. Προεπιλογή είναι η ρύθμιση smart-teach, ωστόσο ο παίκτης μπορεί να το παίξει απλά στο smart. Σε κάθε περίπτωση, μετά επιστρέφει στο 
    κεντρικό μενού.
    Αν επιλέξει 3: Παιχνίδι. Tο πρόγραμμα του ζητάει το όνομά του, μοιράζει γράμματα στους παίκτες και παίζει πρώτος ο άνθρωπος. Καλείται η run. 
    Αν επιλέξει q: Έξοδος από το πρόγραμμα.
    Αν επιλέξει οτιδήποτε άλλο, εμφανίζεται σχετικό μήνυμα και επιστρέφει στο κεντρικό μενού.

    run(): Αρχικά, εμφανίζονται πόσα γράμματα υπάρχουν στο σακουλάκι. Έπειτα, ο άνθρωπος δίνει μια λέξη, η οποία ελέγχεται, μετριούνται οι πόντοι της, αν είναι έγκυρη και 
    μετά ελέγχεται και για το αν είναι η καλύτερη επιλογή. Αν δεν είναι, εμφανίζεται ποια λέξη είναι η καλύτερη επιλογή και πόσους πόντους έχει. (στο smart-teach, στο smart δεν 
    δίνεται η καλύτερη επιλογή και οι πόντοι της). Μετά είναι η σειρά του υπολογιστή.

    give_letters_player(): Δίνει γράμματα στους παίκτες καλώντας την μέθοδο getletters της κλάσης SakClass και την giveletters της Player.

    end(): Καλείται στις εξής περιπτώσεις: όταν ο άνθρωπος πατήσει q (quit), όταν ο υπολογιστής δεν μπορεί αν βρει λέξη για αυτόν και όταν ο υπολογιστής δεν μπορεί να βρει
    καμία λέξη που θα μπορούσε να γράψει ο άνθρωπος. Νικητής είναι αυτός με τους περισσότερους πόντους και εμφανίζονται σχετικά μηνύματα για κάθε περίπτωση. Αν δεν υπάρχει αρχείο
    αποθήκευσης δεδομέων των προηγούμενων παιχνιδιών, δημιουργείται και εγγράφονται στοιχεία όπως αριθμός παιχνιδιού, ημερομηνία, όνομα παίκτη-ανθρώπου, κινήσεις και πόντοι.
    Αν υπάρχει τέτοιο αρχείο, διαβάζονται τα δεδομένα του και προστίθονται τα δεδομένα του παιχνιδιού που μόλις τελείωσε. Σε κάθε περίπτωση, εμφανίζεται μήνυμα για το ότι
    τελείωσε το παιχνίδι και για το αν δημιουργήθηκε ή ενημερώθηκε το αρχείο.

    ΔΟΜΗ ΛΕΞΕΩΝ
    Ο κώδικας μπορεί να δημιουργήσει ένα λεξικό από ένα αρχείο λέξεων (filename) στην κλάση Language. Σε αυτήν την περίπτωση χρησιμοποιείται το greek7. Διαβάζοντας τις λέξεις 
    που περιέχει, κατασκευάζει ένα λεξικό που έχει ως κλειδιά τα πρώτα γράμματα των λέξεων και ως τιμές λίστες με όσες λέξεις ξεκινούν από το εκάστοτε γράμμα. Με αυτόν τον τρόπο,
    ο έλεγχος για το αν μια λέξη ανήκει στο λεξικό ή όχι, και η εύρεση λέξης για τον υπολογιστή γίνονται πιο γρήγορα. Αντίθετα, αν είχε χρησιμοποιηθεί η δομή της λίστας, ο κώδικας 
    θα αργούσε σε αυτά τα σημεία. Αυτό συμβαίνειι, επειδή σε ένα λεξικό  η αναζήτηση ενός δεδομένου γίνεται σε σταθερό χρόνο ανεξάρτητα από το πλήθος των δεδομέων. Είναι δηλαδή
    της τάξης 0(1). Οι λίστες, από την άλλη, είναι της τάξης 0(n).

    
    ΑΛΓΟΡΙΘΜΟΣ PLAY
    Σενάριο 5|Smart-Teach. Ο παίκτης μπορεί να επιλέξει αν θέλει να παίξει το παιχνίδι στο smart ή στο smart-teach μέσα από τις ρυθμίσεις του κεντρικού μενού.
    Smart: Ο αλγόριθμος κάνει όλες τις μεταθέσεις 2 εως 7 γραμμάτων με την βοήθεια της βιβλιοθήκης itertools. Φιάχνει μια λίστα που περιλαμβάνει όλες τις μεταθέσεις,
    ενώνει τα γράμματα από τις μεταθέσεις δημιουργώντας λέξεις και ελέγχει ποιές από αυτές ανήκουν στον λεξικό. Αν ανήκει, μετράει τους πόντους της και φτιάχνει ένα λεξικό
    που έχει ως κλειδιά τις λέξεις και ως τιμές τους πόντους της κάθε μίας αντίστοιχα. Αν το λεξικό είναι κενό, τότε δεν υπάρχει καμία αποδεκτή λέξη και ο υπολογιστής θα 
    πάει πάσο. Αν το σακουλάκι είναι άδειο, δηλαδή δεν μπορεί να πάει πάσο, το παιχνίδι τελειώνει. Αν το λεξικό, δεν είναι κενό, κατασκευάζεται μια λίστα με τις τιμές του λεξικού 
    και παίρνουμε την μέγιστη τιμή, δηλαδή τους περισσότερους πόντους. Μέσω του δείκτη της τιμής, γυρνάμε στο λεξικό και βρίσκουμε σε ποια λέξη αντιστοιχεί. 
    Smart-Teach: Σε αυτήν την επιλογή, ο υπολογιστής παίζει με τον ίδιο τρόπο, μόνο που κάθε φορά που δίνει μια λέξη ο άνθρωπος, αφού γίνουν οι απαραίτητοι έλεγχοι για αυτήν, 
    ο υπολογιστής του λέει ποια θα ήταν η καλύτερη επιλογή. Αν η λέξη που έδωσε ο άνθρωπος είναι η καλύτερη επιλογή, εμφανίζεται μήνυμα που τον συγχαίρει. 

    ΕΝΔΙΑΜΕΣΗ ΑΠΟΘΗΚΕΥΣΗ ΔΕΔΟΜΕΝΩΝ ΤΟΥ ΠΑΙΧΝΙΔΙΟΥ
    Στο αρχικό μενού ο παίκτης μπορεί να επιλέξει να δει τα scores, δηλαδή στατιστικά προηγούμενων παιχνιδιών, όπως ποιός έπαιξε, πόσες κινήσεις έγιναν και πόσους πόντους
    είχε ο παίκτης και πόσους ο υπολογιστής. Η αποθήκευση αυτή γίνεται με encoding utf-8, για να διαβάζονται οι ελληνικοί χαρακτήρες. Ακόμη, τα δεδομένα αποθηκεύονται σε αρχείο json
    εξ'αιτίας των πλεονεκτημάτων που παρουσιάζουν αυτά τα αρχεία σε σχέση με τα pickle. Για το serialization(μετατροπή δομής δεδομένων σε ροή bytes), τα αρχεία pickle χρησιμοποιούν 
    δυαδικές (binary) αναπαραστάσεις, ενώ τα json κείμενο. Έτσι, η μέθοδος serialization καθιστά τα json πιο γρήγορα και πιο εύχρηστα αφού μπορώ πιο εύκολα να ανοιχθούν
    και να διαβαστούν. Επιπλέον, κατά την διάρκεια του deserialization (μετατροπή ροη bytes σε δομή δεδομένων),λόγω του δυαδικού κώδικα των pickle, μπορεί να καλεστούν συναρτήσεις 
    που μπορεί να είναι επιβλαβείς. Αυτό καθιστά τα json αρχείο πιο ασφαλή, διότι δεν έχουν τέτοια κενά ασφάλειας. Επίσης, τα αρχεία pickle είναι συμβατά μόνο με προγράμματα python 
    που μοιράζονται ακριβώς την ίδια δομή. Αντίθετα, τα json μπορούν να διατεθούν ευρέως. Το μειονέκτημα των json είναι ότι τα κλειδιά της δομής πρέπει να είναι
    υποχρεωτικά συμβολοσειρές και οι τιμές ακέραιο, δεκαδικοί, συμβολοσειρές, λίστες και λεξικά. Έτσι, οι πλειάδες μετατρέπονται σε λίστες ενώ άλλοι τύποι δεδομένων (π.χ. μιγαδικοί) 
    δεν γίνονται δεκτοί. Ωστόσο, αυτό δεν εμπόδισε την σωστή αποθήκευση των στατιστικών των παιχνιδιών. 
 


    ΑΡΧΕΙΑ ΑΠΟ ΤΑ ΟΠΟΙΑ ΑΠΟΤΕΛΕΙΤΑΙ Η ΕΡΓΑΣΙΑ
    1)classes.py (βιβλιοθήκη)
    2)main16842
    3)greek7

    '''
guidelines.__doc__
