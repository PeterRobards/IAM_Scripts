#   new_pass:  creates new random password using SHA to hash the date, run it through base64, and
#   outputs the top X characters (by default X = 16, but function accepts X as an input parameter).
#       Note: Good for generating quick temporary or default user passwords on the command line
#             For slightly more secure options see the included python program 
#             * requires sha256sum
# ---------------------------------------------------------
new_pass() {
        p_size=16; pass=""
        ran_pass() { pass=$(date +%s | sha256sum | base64 | head -c $p_size); }
        if [ $# -eq 0 ] ; then ran_pass ; echo "$pass";
        else
                p_size=$1; ran_pass ; echo "$pass"
        fi
}
