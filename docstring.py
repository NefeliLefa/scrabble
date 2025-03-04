def guidelines():
    '''
    SCRABBLE 
    
    ΚΛΑΣΕΙΣ
    
    SaKClass:
    Κλάση που ετοιμάζει το σακουλάκι του παιχνιδιού, δημιουργώντας ένα λεξικό που έχει ως κλειδί ένα γράμμα και ως τιμή την αξία του γράμματος στο scrabble. 
    Έτσι, κάθε γράμμα μέσα στο λεξικό, έχει ως δείκτη έναν φυσικό αριθμό. Με βάση αυτους τους δείκτες θα γίνεται και η τυχαία επιλογή γραμμάτων για κάθε παίκτη, μέσω 
    τηςσυνάρτησης randint. Αν το σακουλάκι έχει λιγότερα γράμματα από αυτά που δικαιούται ο παίκτης, τότε ο παίκτης παίρνει όλα τα γράμματα που έχει το σακουλάκι.
    Επίσης, η κλάση αυτή έχει μια συνάρτηση για να επιστρέφονται γράμματα στο σακουλάκι, και μία για να παίρνουμε το πόσα γράμματα έχουν μείνει στο σακουλάκι, το
    οποίο φαίνεται και μέσω της αναπαράστασης της κλάσης.

    Language:
    Κλάση που φτιάχνει το λεξικό που θα χρησιμοποιηθεί για το παιχνίδι. Το λεξικό έχει ως κλειδιά τα γράμματα του αλφάβητου και ως τιμές λίστες με όλες τις λέξεις 
    που αρχίζουν από αυτό το γράμμα με βάση του αρχείο .txt που επιλέγουμε. Ακόμη, ελέγχει αν μια λέξη ανήκει σε αυτό το λεξικό.

    Payer:
    Βασική κλάση (υπερκλάση) των Human & Computer. Δίνει το όνομα Pc στον υπολογιστη και ζητάει όνομα από τον άνθρωπο-παίκτη. Δίνει γράμματα στους παίκτες και τα 
    παρουσιάζει με την αξία του κάθε γράμματος από δίπλα. Δείχνει τους πόντους που έχει ο κάθε παίκτης. Επιπλέον, καλύπτει την περίπτωση που ένας παίκτης πάει πάσο. Περιλαμβάνει,
    συνάρτηση που βρίσκει κάθε πιθανή λέξη κάνοντας μεταθέσεις στα γράμματα και επειτα ελέγχει για κάθε λέξη αν ανήκει στο λεξικό. Έπειτα, μέσα από μία άλλη συνάρτηση,
    υπολογίζουμε τους πόντους που πιάνει κάθε λέξη και διαλέγουμε αυτήν με τους περισσότερους. 

    Human:
    Παράγωγη κλάση του Player. Περιγράφει το πώς παίζει ο άνθρωπος, ελέγχει αν η λέξη που δίνει είναι σωστή. Συγκεκριμένα αν μπορεί να γραφεί με τα γράμματα που έχει ο παίκτης και αν 
    ανήκει στο λεξικό. Έπειτα υπολογίζει τους πόντους της. Στην συνέχεια, έχει συνάρτηση η οποία μαθαίνει στον παίκτη ποια είναι η καλύτερη λέξη θα μπορούσε να είχε γράψει με τα γράμματα 
    που έχει.

    Computer:
    Παράγωγη κλάση του Player. Περιγράφει το πώς παίζει ο υπολογιστής χρησιμοποιώντας κυρίως συναρτήσεις της υπερκλάσης Player.

    Game:
    Κλάση διαμεσολαβητή μεταξύ των κλάσεων, που περιγράφει πώς εξελίσσεται μια παρτίδα. Στην αρχή ο χρήστης καλείται να διαλέξει αν θελει να δει τα προηγούμενα σκορ, αν θέλει να μεταβεί 
    στις ρυθμίσεις,αν θέλει να παίξει ή αν θέλει να βγει από το παιχνίδι. Αν επιλέξει 3: Παιχνίδι, τότε το πρόγραμμα του ζητάει το όνομά του, μοιράζει γράμματα στους παίκτες και παίζει 
    πρώτος ο άνθρωπος.Αρχικά, εμφανίζονται πόσα γράμματα υπάρχουν στο σακουλάκι. Έπειτα, ο άνθρωπος δίνει μια λέξη, η οποία ελέγχεται, μετριούνται οι πόντοι της, αν είναι έγκυρη και 
    μετά ελέγχεται και για το αν είναι η καλύτερη επιλογή. Αν δεν είναι, εμφανίζεται ποια λέξη είναι η καλύτερη επιλογή και πόσους πόντους έχει. Μετά είναι η σειρά του υπολογιστή.

    ΔΟΜΗ ΛΕΞΕΩΝ
    Ο κώδικας μπορεί να δημιουργήσει ένα λεξικό από ένα αρχείο λέξεων (filename) στην κλάση Language. Σε αυτήν την περίπτωση χρησιμοποιείται το greek7. Διαβάζοντας τις λέξεις 
    που περιέχει, κατασκευάζει ένα λεξικό που έχει ως κλειδιά τα πρώτα γράμματα των λέξεων και ως τιμές λίστες με όσες λέξεις ξεκινούν από το εκάστοτε γράμμα. Με αυτόν τον τρόπο,
    ο έλεγχος για το αν μια λέξη ανήκει στο λεξικό ή όχι, και η εύρεση λέξης για τον υπολογιστή γίνονται πιο γρήγορα. Αντίθετα, αν είχε χρησιμοποιηθεί η δομή της λίστας, ο κώδικας 
    θα αργούσε σε αυτά τα σημεία.
    
    ΑΛΓΟΡΙΘΜΟΣ PLAY
    Σενάριο 5|Smart-Teach. Ο παίκτης μπορεί να επιλέξει αν θέλει να παίξει το παιχνίδι στο smart ή στο smart-teach μέσα από τις ρυθμίσεις του κεντρικού μενού.
    Smart: Ο αλγόριθμος κάνει όλες τις μεταθέσεις 2 εως 7 γραμμάτων με την βοήθεια της βιβλιοθήκης itertools. Φιάχνει μια λίστα που περιλαμβάνει όλες τις μεταθέσεις,
    ενώνει τα γράμματα από τις μεταθέσεις δημιουργώντας λέξεις και ελέγχει ποιές από αυτές ανήκουν στον λεξικό. Αν ανήκει, μετράει τους πόντους της και φτιάχνει ένα λεξικό
    που έχει ως κλειδιά τις λέξεις και ως τιμές τους πόντους της κάθε μίας αντίστοιχα. Αν το λεξικό είναι κενό, τότε δεν υπάρχει καμία αποδεκτή λέξη και ο υπολογιστής θα 
    πάει πάσο. Αν το σακουλάκι είναι άδειο, δηλαδή δεν μπορεί να πάει πάσο, το παιχνίδι τελειώνει. Αν το λεξικό, δεν είναι κενό, κατασκευάζεται μια λίστα με τις τιμές του λεξικού 
    και παίρνουμε την μέγιστη τιμή, δηλαδή τους περισσότερους πόντους. Μέσω του δείκτη της τιμής, γυρνάμε στο λεξικό και βρίσκουμε σε ποια λέξη αντιστοιχεί. 
    Smart-Teach: Σε αυτήν την επιλογή, ο υπολογιστής παίζει με τον ίδιο τρόπο, μόνο που κάθε φορά που δίνει μια λέξη ο άνθρωπος, αφού γίνουν οι απαραίτητοι έλεγχοι για την λέξη που
    έδωσε, ο υπολογιστής του λέει ποια θα ήταν η καλύτερη επιλογή. Αν η λέξη που έδωσε ο άνθρωπος είναι η καλύτερη επιλογή, εμφανίζεται μήνυμα που τον συγχαίρει. 


    ΑΡΧΕΙΑ ΑΠΟ ΤΑ ΟΠΟΙΑ ΑΠΟΤΕΛΕΙΤΑΙ Η ΕΡΓΑΣΙΑ
    1)classes.py (βιβλιοθήκη)
    2)main16842
    3)greek7
    '''