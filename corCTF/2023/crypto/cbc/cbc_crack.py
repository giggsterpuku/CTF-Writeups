#!/usr/bin/env python3

def sub_key(key, block): # reverse action of add_key
	ct_idxs = [(ct_a - k_a) % len(alphabet) for k_a, ct_a in zip([alphabet.index(k) for k in key], [alphabet.index(ct) for ct in block])]
	#print(ct_idxs) # used to get all the indexes of the blocks with the IVs "subtracted from them" (more like undoing Vignere's cipher)
	return "".join([alphabet[idx] for idx in ct_idxs])

def decrypt_cbc(iv, ciphertext):
	blocks = [ciphertext[i:i+bs] for i in range(0, len(ciphertext), bs)]
	#print(sub_key("RJECTFORAMOMENTW",sub_key(blocks[0],blocks[1]))) # piece of readable text from Boxentriq, used it to recover the key
	''' # used to recover the key
	prev_block = iv
	plaintext = ""
	for i, block in enumerate(blocks): # decrypt Vigenere's cipher using IV as key first
		blocks[i] = sub_key(iv, block)
	for block in blocks: # now spit the remnants out as a Vegenere ciphertext...and autosolve the key maybe using the Boxentriq website!
		tmp = block
		plaintext += sub_key(prev_block,block)
		prev_block = tmp
	'''
	prev_block = iv
	plaintext = ""
	for block in blocks:
		tmp = block
		block = sub_key(key, block)
		plaintext += sub_key(prev_block,block)
		prev_block = tmp
	return plaintext

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bs = 16
iv = 'RLNZXWHLULXRLTNP'
ct = 'ZQTJIHLVWMPBYIFRQBUBUESOOVCJHXXLXDKPBQCUXWGJDHJPQTHXFQIQMBXNVOIPJBRHJQOMBMNJSYCRAHQBPBSMMJWJKTPRAUYZVZTHKTPUAPGAIJPMZZZDZYGDTKFLWAQTSKASXNDRRQQDJVBREUXFULWGNSIINOYULFXLDNMGWWVSCEIORQESVPFNMWZKPIYMYVFHTSRDJWQBTWHCURSBPUKKPWIGXERMPXCHSZKYMFLPIAHKTXOROOJHUCSGINWYEILFIZUSNRVRBHVCJPVPSEGUSYOAMXKSUKSWSOJTYYCMEHEUNPJAYXXJWESEWNSCXBPCCIZNGOVFRTGKYHVSZYFNRDOVPNWEDDJYITHJUBVMWDNNNZCLIPOSFLNDDWYXMYVCEOHZSNDUXPIBKUJIJEYOETXWOJNFQAHQOVTRRXDCGHSYNDYMYWVGKCCYOBDTZZEQQEFGSPJJIAAWVDXFGPJKQJCZMTPMFZDVRMEGMPUEMOUVGJXXBRFCCCRVTUXYTTORMSQBLZUEHLYRNJAAIVCRFSHLLPOANFKGRWBYVSOBLCTDAUDVMMHYSYCDZTBXTDARWRTAFTCVSDRVEENLHOHWBOPYLMSDVOZRLENWEKGAWWCNLOKMKFWWAZJJPFDSVUJFCODFYIMZNZTMAFJHNLNMRMLQRTJJXJCLMQZMOFOGFPXBUTOBXUCWMORVUIIXELTVIYBLPEKKOXYUBNQONZLPMGWMGRZXNNJBUWBEFNVXUIAEGYKQSLYSDTGWODRMDBHKCJVWBNJFTNHEWGOZFEZMTRBLHCMHIFLDLORMVMOOHGXJQIIYHZFMROGUUOMXBTFMKERCTYXFIHVNFWWIUFTGLCKPJRFDRWDXIKLJJLNTWNQIOFWSIUQXMFFVIIUCDEDFEJNLKLQBALRKEYWSHESUJJXSHYWNRNPXCFUEFRJKSIGXHFTKNJXSYVITDOGYIKGJIOOHUFILWYRBTCQPRPNOKFKROTFZNOCZXZEYUNWJZDPJDGIZLWBBDGZJNRQRPFFGOTGFBACCRKLAPFLOGVYFXVIIJMBBMXWJGLPOQQHMNBCINRGZRBVSMLKOAFGYRUDOPCCULRBE'

key = "ACXQTSTCSXZWFCZY"

print(decrypt_cbc(iv,ct))
