rule GnuCash
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $GnuCash0 = "gnucash"

    condition:
        $GnuCash0

}

rule GNOME_Keyring_
{

    meta:
        description0 = "repo scanner :  GnuCash database file"

    strings:
        $GNOME_Keyring_0 = "^key(store|ring)$"

    condition:
        $GNOME_Keyring_0

}
