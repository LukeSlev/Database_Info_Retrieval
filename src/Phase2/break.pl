#!/usr/bin/perl
<<<<<<< HEAD

=======
>>>>>>> 098a2a25a371424c36f64e7856b4b0586abf1c75
while (<STDIN>) {
  chomp;
  if (/^(.*?):(.*?)$/) {
    $key=$1; $rec=$2;
    # BDB treats backslash as a special character, and we would get rid of it
    # (if still present)!
    $rec =~ s/\\/&#92;/g;
    print $key, "\n", $rec, "\n";
  }
}
<<<<<<< HEAD

=======
>>>>>>> 098a2a25a371424c36f64e7856b4b0586abf1c75
