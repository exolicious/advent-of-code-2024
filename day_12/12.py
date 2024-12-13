

import sys


input = """SSSSSOOOOOBFFJJFTFBBBBBBBBPPPPPPPPBBBBBBBBBBBSSDDDDDDCCCCCCCCCCCUUUUUAAAAAAAAAAAAAAAUUUUUUUUUUUUUUUUUUUUUUDDDDDDMMMMMZZFFZZFFFFFFFFFFFFFFFII
SSSOOOOOFFFFFFJFFFFBBBBBBBPPPPPPPPPBBBBBBBBBSSSSSSSSDDCCCCCCCCCUUUUUUUUAAAAAAAAAAAAAUUUUUUUUUUUUUUUUUUUUUUUDDDDDMMMMZZZZFZZFFFFFFFFFFFFFFFII
OOSOOOOOFFFFFFJFFFFBBBBBBPPPPPPPPPPBBBBBBBBBBSSSSSSSDCCCCCCCCUUUUUUUUUUUUAAAAAAAAAAUUUUUUUUUUUUUUUUUUUUUUDDDDDDDDDDZZZZZZZFFFFFFFFFFFFFFFFII
OOOOOOOOFFFFFFFFFFFHBBBBBBPPPPPPPPPBBBBBBBBBBSSSSSSSDCCCCCCCUUUUUUUUUUGGUAAAAAAAAAUUUUUUUUUUUUUUUUUUUUUDVDDDDDDDDDDZZZZZZZZFFFFFFFFFFFFFFFII
OOOOOOOOOFFFFFFFFFFFFBBBBPPPPPPPPPPPBBBBBSSSSSSSSSSSDXXCYCCCUUUUUUUUUUUUUAAXXAAAAUUUUUUUUUUUCUUUUUUUUUUDDDDDDDDDRDHZZZZZZZZFFFFFFFFFFFFFFFII
OOOOOOOOOOFFFFFFFFFFFFFFBPPPPPPPPPPPBPPPBBSSSSSSSSXXXXXCXXCCUUULUUUUUUUUUUAXXXAAAUUUUUUCCCCCCCCCSUUUUUUDDDDDDDDFRRFZZZZZZZZZZZFFFFFFFFFFFFII
OOOOOOOOOOFFFUFFFFFFFFFFIPPPPPPPPPPPBBPPBBSSSSSSSMMMXXXXXXWUUUUUUUUUUUUUUCXXXXXXXWWWUUCCCCCCCCCCSUUUUUDDDDDDDDXFFFFZZZZZZZZZZZFFFFFFFFFFFFII
COOCOOOOOOKFFUFUUUFFFFFIIPPPPPPPPPPPPPPPPPSSSSSSSSMXXXXXXXUUUUUUUUUUUUUUUUUUXXXXXXXWWWCCCCCCCCCCSSSUUUUUDDDDDDFFFKFFZZZZZZZZFFFFFFFFFFFFIIII
COCCCOOOOOKFUUUUUUFFFFFIIIIPPPPPPPPPPPPPPIITSSSSSIXXXXXXXXUUUUUUUUUUUUUUUXXXXXXXXXWWWWWCCCCCCCCSSSSSSSSUUDDDDDFFFFFFZZZZZZZZFFFFFFFFFQQQIIII
CCCCCCCOKOKKUUUUUUFFFFFIIIIPPPPPPPPPPPPPPIIIIISIIIIXXXXXXXUUUUUUUUUUUUUUUXXXXXXXXXWWWCCCCCCCCCGSSSSSSSSSUDDDDFFFFFFFZZZZZZZZMZFFFXFSQQFQQQII
CCCCCCCCKKKKKKUUUUFUUKKIIIIPPPPPPPPPPPPPPIIIIIIIIIIIIIXXXXXURUUUUUUNUNUUXXXXXXXXXXWWWWCCCCCCCCSSSSSSSSSKKDDDDFFFFFFZZZZZZZZZZZXFFXFFFQQQQQII
CCCCCCKKKKKKKKUUUUUUKQKKIIIIIPPPPPPPPPPPPIIIIIIIIIIIIIXXXXXURUKKUUNNNNUXXXXXXXXTXXWCCCCCCCCCCCISSSSSSSSKKKKDDSFFFZZZZZZZZZZZZZXXXXFQQQQQQQQI
CCCCCCCCKKKKKKUUUUUUKKKKKLLIIPPPIPPPPPPPPPIIIIIIIIIIIIXXXXXXRSSSUUNNNNUNXXXXXXZXXWWCCCCCCCCCSSSSSSSSSSSSSKKKDSSZZZZZZZZZZZZZZZXXXXFFGQQQQQQQ
CCCCCCCCCCUKKKUUUUUUUUKKLLLIPPPIIIPPPPPPPIIIIIINIIIIIIIIXXXXSSSSNNNNNNUNXXXXXXZXXXCCCCCCCCCCCSSSSSSSSSSSSKKKSSSZZZZZZZZZZZZFFFFFXXFFFQQQQQQQ
CCCCCCCCCUUUUKUUUUUUULKKLLLLLIIIIIPPPPPPPIIIIKKNIIIINIIIISXXSSSSGGGNNNNNNNXQZZZZZXXXXCCCXCSCCCSSSSSSSSSSSKKKSSSSZZZSZZZZZZZFDFFFFFFFWQQQQQQQ
CCCCCCCCCUUUUUUUUUUUULLLLLLLLLLIIIPPPPPPPKIIKKBNNNNNNNNSSSUXSSJGGGGGNNNNNQQQZZZXZXXXXCCCXXSSSSSSSSSSSSSSSKKSSSSSZSSSZSZZZFFFDFFFFFFFQQQQQQQQ
CCCCCCCCCUUUUUUUOULLLLLLLFLMLLIIIIPPPPPKKKIEEKKNNNNNNNNSSUUSSSJJGGGNNLNNNQQQQZZXXXXXXXXXXXXXXSSSSTSSSSSKKKKKKSSSSSSSSSSZZJFFDFFFFFFFFQQQQQQQ
CCCCCCCCCUJJJJJJUULLLLLLLLLLIIIIIIPPPKKKKKEEKKKNNNNNNNNNSSSSSSSGGGGNNLNNNQQQQQXXXXXXXXXXXXXXXTSSSTSSSSSKKKKKSSSSSSSSSSSZZFFFFFFFFFFFFQQQQQQQ
CCCCCCKKKUUJJJJJJJLLLLLLLLLLLIIIIIIPKKKKKKKKKKKNNNNNNNNNSSSSSSSGGGGGGLLLNQQQQQQQXXXXXXXXXXXXXTSTTTTTSSSKKKKSSSSSSSSSSSSSSSFFFFFFFFFFQQQQQQQQ
CCCCFFFFFFJJJJJJJLLLLLLLLLLLLLIIIIPPKKKKKKKKKKNNNNNNNNNXXXSSMMMGGGLLLLLLNQNQQQQQXXXXXXXXXXXXXTTTTTTTTTSHKKSSSUSSSSSSSSSSSZFFFFFFFFFFQQQQQQQQ
CCCCFFFFFFFJJJJJJLLLLLLLLLLLLLIIIHHPPKKKKKKKKKKKNNNNNNNNXXXSMMLLLLLLLLLNNNNNQQQQQXXXXXXXXXTXTTTTTTTTTTTHKSSSSSSSSSSSSSSSSSFFFFFFFFFQQQQQQQQQ
CCCCFFFFGFFJJJGJJJJJLLLLLKKLLLIIIHHKKKKKKKKKKKKKNNNNNNNXXXXSMMMLLLLLLLLNNNNNQQQQQQXXXXXXXXTTTCCTTTTTTTHHHHHDSSLSSLSSSSSSSSFFFFFFFFFQQEEQQQQQ
CCFGFFFFFFFFGGGJGJJLLLLLUEELILIIIKKKKKKKKKKKIKKUNNNNNNXXXXXXXLLLLLLLLLLLQQQQQQQQQQQXXXXXXXXCTCTTTTTTTTTHHHHHIILLLLSSSSSSHHHFHFFFFFFEEEEEQEQQ
CCFFFFFFFFFFGGGGGJJLLLLLUEESIIIIIIDDKKKKKKKKUUUUNNNNNNXXXXXXZZLLLLLLLLLLLQQQQQQQQQQQXXXXXXJCCCCTTTTTTTTHHIIHIIIWLLSSSQQSHHHHHHFFFFFFEEEEEEQQ
XFFFFFFFFFFFGGGGGGJHLLLLUEEIIIIIIIDDDDKYKKKKKUUUUNUUNNCXXXXXXZZLLLLLLLLBLMBQQQQQQQQQXXCCCXCCCCCTTTTTTTHHHIIIIIWWQQQQQQQSSHHHHHFFFPPFEEEEEEQQ
FFFFFFFFFFFGGGRGGPHHLHHLLEEEIIIIIDDDDDUYYKKKKUUUUUUUWWXXXRXXXKKKKKKLLLBBBBBQQQQQQQCCXXCCCCCCJCCTTTTTTTTHFIIIIIIWWQQQQQQJHHHHHHHJJPEEEEEEEIEQ
FFFFFFFFFCFFFGRRPPHHHHHELEEEEEEIDDDDDUUUYYYKUUUUUUUWWWWWXXXKKKKKKKLLLBBBBBBQQQQQQQQCCCCCCCCCCCCFTTTTFTTFFFIFIWWWWQQQEQQJJHHHHHJJJJJJXEEEEEEQ
FFFFFFFFFFRFRRRRPPHHHHEEEEEEEEEEEDDDDUUUUUKKUUUUUUWWWWWWXKKKKKKKKKLLLBBBBBBQQQQQQQCCCCCCCCCCCCGFFFFFFFTFFFIFIWWWWEEQEQQJJJHJJJJJJJJJJJREQQEQ
FFFFFFFFFFFFFFPPPPPHPEEQEEEEEEEEEEDEUUUUUUUUUUUUUUUWWWWWWKKKKKKKKKKLLBKBBBBBBQQQQCCCCCCCCCCCCCCAFFFFFFFFFIIFIIIWWEEEEQJJJHHJJJJJJJJJJJJJJQEQ
FFFFFFFFFFFFPPPPPPPPPEEEEEEEEEEEEEEEUUUUUUUUUUUUUUUWOXXXXKKKKKKKKKLLLBBBBBBBBBBQQCCCCCCCCCCCCCCCFFCCCFCFFFFFFFFWWEEEEEJJJJJJJJJJJJJJJJJJJQQQ
FKFFFFFFFFFFFPPPPPPPPPEEEEEEEEEEEEEEUUUUUGUUUUUUUWUWOVVXXKKKKKKKKKLBLBBBBBBBBBQQQCCCCCCCCCCCCCCCFCCCCCCFFFFFFFFWEEEWWEJJJJJJJJJJJJJJJQJQJQQQ
KKFFFFFFFFFFFPPPPPPPPPPEEEEEEEEEEHELLLUUUGUUUUUWWWWWOOOXXXWWKKKKKILBBBBBBBBBBOQQQQCCCCCCCCCCCCCCCCCCCGCFFFFKKKAWWWWWWWWJJJJJJJJJJJJJJJJQJQQQ
KKKKKFFFFFKFPPPPPPPPPPEEEEEEEEEEEELLLLLGGGGUUUUWWPWOOCOOOXWWKKKKKIBBBBBBBBBBBOOQQCCCCCCCCCCUUUCCCCCGGGGFFFKKKAAAAAWWWWWWJJJJJJJJJJJJQQQQQQQQ
KKKKKFFFFFKKKPPPPGGGGPIEEEEEEEEEELLLLLLLGRRRUCUPPPPOOOOOOOWWWKKKIIIBBBBBBBBBBBOQOCCCCCCCCCUUUUUCCGGGGGGFCEAAAYAAAAWWAAWWJJJJJJJJJJJJJQRQQQRQ
KKKKKKFFKFKKPPPGGGGTTEEEEEEEEEEEELLLLRRLLRRRRUUNPPPVOIORROWXXXMKKXXBBBBBBBBBBBOOOOOOCCCCCUPUUUUUUGGGGGCCCAAAAAAAAAAAAAWWNJJJJJJJJJJJJQRRQRRQ
KKKKKKFKKKKKKPPGGGGGGGSSSSEEEEEQUUUURRRRRRRRGGGPPPVVPPKRRWWXXXMKXXXBBBBBBBBBBBOOOOOOCCCUUUPUUUUUUUGGGGGCCAAAAAAAAAAAAAANNNNJJJJJJJJJQQRRRDRR
KKKKKKKKKKKKKGGGGGGGGGGSSSEPEEEQUUUUUURUUUUUGGPPPPVPPNRRRRRXXXXXXXXXBBBBBBBBBBBBBOOOOOUUVUUUUUUUYYGGGGRCCAAAAAAAAAAAAAANNNNNNJJJJJQQQRRRRRRR
KKKKKKTKKTKKTTSSGGSGSGGSSSPPFEZUUUUUUUUUUUUUPGPPPPPPPPBRRRRXXXXXXXXXXBXBBBBBBBBBBBOOOOUUUUUUUUUUUUAAGGRCAAAAAAAAAAAAAAAGNNNNNJJJJJQQRRRRRRRR
KKKKTTTTTTTTTTSSGGSSSSSSSSPPFPZUUUUUUUUUUUUPPPPPPPPPMPRRREEXXXXXXXXXXXXBBBBBOBBBOOOOOUUUUUUUUUUUUAAGGGGAAAAAAAAAAAAAAAAANNNNNNJJJJJJRRRRRRRR
KKKKKTWTTTTTTTTSSSSSSSPSPPPPPPUUUUUUUUUUUUUUPPPPPPPPPKRRREXXXXXXXXXXXXXVBBBOOOOOOOOOOUUUUUUUKUUUUAAGVVVVAAAAAAAAAAAAAUUUNNNNNNJJJJJRRRRRRRRR
KKKKKTTTTTTTTTTSSSSSSSPPPPPPPPJUUUUUUUUUUUUPPPPPPPPPPPPPPEEXXXXXXXXXXXXXXFBEEOOOOOOOAUUUAAUUUUUDAAAWYVYAAAAAAAAAAAAAAUUUNNNNNNNRRRRRRRRRRRRR
KKKKTTTTTTTTTTTSSSSSSSPPPPPPPPPURUUUUUUUUUPPPPPPPPPPPRPPPEEEEEXXXUXXXXXXXFFEEOOOOOOOAUUUAAUAUUUAAAAWYYYYYAIAJAAAAAUUUUNNNNNNNNNTRRRRRRRRRRRR
KKKKTTTTTTTTTTSSSSSSPPPPPPPPPPSSUUUUUUUUUUUPSPPPPPPPPPPJPREEEEXXXUUXXXXXCEEEOOOOAOAAAAAAAAAAAUAAAAAYYYYYYQAAAAAAAAUUUUUNNAANNIITTRTRRRRRRRRR
KKKKKTTTTTTSSSSSSSSPPPPPPPPPPPPPPUUUUUUUUUGPPPPPPPPPPPJJJRRRRRXXXOUUUXXXCEEEOOOOAAAAAAAAAAAAAAAAAAAYYYYYYYYYAAAAAAUUUUUUUATTTTTTTTTRRRRRRRRR
KKKKKTTTTTTSSBSSSSSSSPPPPPPPPPPPUUUUGGUUUGGGGGPPPPPJJJJJRRRRRRRRUUUUUSXCCEEEOOOGAAAAAAAAAAAAAAAAAYYYYYYYYYBYYBBAAUUUUUUUUUTTXTTTTTTTTRRRRRRR
KKBKBBTTTTBBBBSSSSSSSSPPPPPPPPPPPUUGGGCGUGGGGGPPPPJJJJJJJRRRRRUUUUUUUUXUEEEEEEEGGAAAAAAAAAAAAAAAAYYYYYYYYYYYBBBBUUUUUUUUUTTTTTTTTTTBBBBRRRRR
KBBBBBBTTBBBBBSSSSSSSSPPPPPPPPPPPPUJGGCGGGGGGGGPXPPJJJJJRRRRRRUUUUUUUUXUVEEEEEEGGGGAAASAAAAAAAAAAYYYYYYYYYYBBBBBUUUUUUUUUTTTTTTTTTTBBBBRRRRR
KKKBBBBBTBBBBBSSSSSSSSPXPPPPPPPPPSSGGGGGGGGGGGPPPPZZZZJJZZNRRRUUUUUUUUUUUEEEEGGGGGIIIIAAEUUUUAAAAYYYYYYYYYYBBBBUUUUUUUUUBBBTTTTTTTTTBBBRRRRR
KKBBBBBBBBBBBBBSSSSSPPPPPPPPPYPSPSSSGSGGGGGGGGPPPZZZZZJZZNNNRRRUUUUUUUUUEEEEEEGGIIIISAAAUUUUWAACYYYYYYYYYYYBBBBBUUUUUUUUBBTTTTTTTTTBBBBRRRRR
KKKBBBBBBBBBRBBBBSSSSSPPPPPPPPSSPPSSSSGGGGGGGGPPZZZZZZZZNNNUUUUUUUUUUUUUUEEEEEEEEEIIIIAAUUUIWAAYYYYYYYYYPBBBBBBBBUUUUUUUBBTTTTTTOOTBBBBRRRRR
OOKKBBBBBBBBBBBBSSSSSSPPPPPPPPSSPPSSSSGGSGGGGGGZZZZZZZPZNNNUUUEEUUUUUUUEEEEEEEEEEIIIIAAIIIIIIIIIIIYYYYYYPBBBBBBBBBBUUUBBBBBBYYYYOONNNBRRRRRR
OOOOOOBBBBBBBBBBBBSSSSPPPKPMPPSSSSSSSSSSSGGGGGGZZZZVVZZNNNNNNEEEUUULUUUULLEEEEEEEIIIIIIIIIIIIIIIIIYYYYPPPBBBBBBBBBBBBBBBBBBBYOYYOONNNNPRRPRP
OOOOOOBBBBBBBBBBBFVSSSPMMMMMMMSSSSSSSSSSSGGGGGGCCZZVZYZNNWWNWEEEUULLULLLLLEEEEEEEIIIIIIIIIIIIIIIIIYYYYQPPBPBBBBBBBBBBBBBBBBBBOYOOOONVVPPPPRP
OOOOOOOBBBBBVVBVTVVSSVMMMMMMMSSSSSSSSSSSGGGGGXCCCCZZZZKKKKKKKKKKELLLLLLLLLEEEEEEEIIIIIIIIIIIIIIPIIIUUPPPPPPBBBKBBBBJJJBBBBBOOOOOOOONVVPPPPPP
OOOOOOOBBBBBVVVVVVQVSVMMMMMMMSSSSSSSSSSSSVGGGXXCMMZZZZKKKKKKKKKKELLLLLLLLEEEEEEEEIIIIIIIIIIIIIIPPPPPPPPPPBBBKBKKKKBJJJBBBBOOOOOOOOONVVPPPPPP
OOOOOOOOOBXVVVVVVVVVVVVMMMMMYSSSSSSSSSSASVVAGXCCMVZMZMKKKKKKKKKKELLLLLLLLLEEEEEIIIIIIIIIIIIIIIIPPPPPPPPPCBBKKKKKKKBJJJBBBBOOOOOOOOOOXXXXPPPP
OOOOOOOOOXXXVVVVVVVVVMMMMMCMSSSSSSSSSSSVVVXGGXMMMVMMMMKKKKKKKKKKQLLLLLLLEEEEIEIIIIIIIIIIIIIIIIIIIPPPPPPPCPBCKKKKKKJJJJJJJJOOOOOOOOOOXXXXXPPP
OOOOOOOOOZXXVVVVVVVVVMTMCMCCSSSSSSSSSSSVVVXXXXMMMMMMMAKKKKKKKKKKLLLLLLLLLLIIIIIIIIIIIIIIIIIIIIIIPPPPPPPPPPBBKKKKKKJJJJJJJJJJJJOOOOOOXXXXXXMM
OOOOOOOOOXXXVVVVVVVVVVVVCCCCCSSSSSSSSSVVVXXXVVMMMMMMMMKKKKKKKKKKLLLLLLLLLKIIIIIIIIIIIIIIIIIIIIIHPPPPPPPPPPBBBKKKKKJJJJJJJJJJJJOOXOOOXXXXXXXM
OOOOOOGOOXXXXXVVVVVVVVVVCCCCCCSSSSSSSSVVVVXXVMMMMMMMMMKKKKKKKKKKLLLLLLLLLKIIKIIIIIIIIIIIIIIIHHHHHPPPPPPPPPQQQQKKKKJJJJJJJJJJJJXXXXXXXXXXXXXM
OOOOOOOOOXXXXXVVVVVVVVVVCCNNCCSSSSSSSSSVVVXXVVMMMMVMMVVVVWWWWWWWLLLLLLLLLKIIKKKIIIIIIIIIIIIIHHHPPPPPPPPPPWOQQQQQQQJJJJJJJJJJJJOSAAXXXXXXXXXM
OOOOOOOOOOXCECCCVVVVVVVCCCNNNCSSSSSSSVVVVVVXVVVMVVVMMVVVVVWWWWWWLLLLLLLLLKKIKKKIIIIIIIIIIIIHHHHPPPPPPPPPXOOQQQQQQQJJJJJJJJJJJJSSWWXXXXXXXXXM
OOOOOOOOOOCCCCCVVVVVCCCCCNNVNSSSSSSVVVVVVVVVVVVMVVVVVVVVVVVLWWWWWLLLLLLLLLKKKCCCCCICIIIIIIHHHPPPPVVVPCCPPOOQQQQQQQJJJJJJJJJJJJSSWWWWXXXXXXXX
OOOOOOOOCCCCCCCCCVVVVCCCCNNNNNNSSSSVVVVVVVVVVNNZZZVVIVVVVVVLLLWWLLLLLLLLOODKKKCCCCCCIIIIBIHHHTTPPOOOCCPPPOOOOOQOXQJJJJJJJJJJJJJSWWWWWXXXXXXX
OOOOOOOOOCYCCCCCCVVVCCCCNNNNNNNSSSSSVVVVVVVVVVNZZZZZIVVVVVVLLLLLLLLLLLLLLDDDDCCCCCCIIIIIIIHHHTTPPFOCCCOOOOOOOOOOXQWWWJJJJJJJJJJSSWWWWXXXXXXR
OOOOOOOOYYYCCCCCCVVCCCCNNNNNNNNNNNVVVVVVVVVVVVNNVVZIIVVVVVVLLLLLLLLLLLLZZDDDZCCCCCCCIIIIIIHHHHHPPFOCCCOOOOOOOOXXXXXXWJJJJJJJJJJSWWWWWWXXXXXX
OOOOOOOYYYYYCCCCCCCCCCCNNNNNNNNNCOVVVVVVVVVVZZNSGVVVVVVVVVVLLLLLLLLLLLLLZDDZZCCCCCCIIIIIIHHHHHHFFFOOOOOOOOOOOOOXXXXXWJJJJJJOSDSWWWWWWWXXXXXX
OOOOOYYYYYYYCCCCCCCCCCCNNNSNNNNNCCVVVVVVVZZVVZFSGGGGVVVVVVVMLLLLLLLLLLLLZZZZZCCCCCCCTIIITTTHHHHFFFOOOOOOOOOOOOOOOXXXXXWXXXOOSDWWWWWWWWWXXXXX
OOOYOYYYYYYYCCCCCSCCCCCCCNNNNNNNCCCVVVVZZZZZZZSSSGGMLVVVVVHMMMMMMLLLLLZZZZZZZZCCCCTTTTITTTTBFFFFFFOOOOOOOOOOOOOXXXXXXXXXXXOOOWWWWWWWWWWXXXXM
OOOYYYYYYYYYYGGCCSSSSCCCNNNNNCCCCCCVVZZZZZZZZZZZZMMMLVVVVMMMRLLBLLFFFFFFFFFFZZCXCCCTTTITTTTBBFFFCFOOOOOOOOOOOOXXXXXXXXXXXXXOOXWWWWWWWWWWWMXM
OOOYYYYYYYYGGGGCCCCSSSCCCNNNNNCCCCKVVNNZZZZZZZZZZZKMMVVVVMMMRLLLLLFFFFFFFFFFZZCCCCZATTTTTTTBFFFCCCOOOOOOOOXXOXXXXXXXXXXXXXWXXXSSSWWWWMMMWMMM
OODBYYYYYYYGGGGGSSSSSSSCCCCCCCCCCCCNNNNNZZZZZZZZZMMMMMMMVMMMMMLOLZFFFFFFFFFFZZZZZZZAATTTTTTBBFCCCOOOOOOOOOOXXXXXXXXXXXXXXXXXXXSSSSWWMMMMMMMM
OBDBBBBBEYSGGGGGSSSSSSSSSCCCCCCCCCNNNNZZZZZZZZZZMMMMMMMMVMMMMMMMMZFFFFFFFFFFZZZZZAAAATTTTBBBFFCCBOOOOOOOOOOOOODDDXXXXXXXXXXXXXSSSSWHHMMMMMMM
BBBBBBBBBGGGGGGSSSSSSSSSCCCCCCCCCCCCZZZZZZZZZZZZMMMMMMMMMMMMMMMMMZZZZZZZZZZZZZZZZAAAAAATTBBBFFBBBIOIZZOZZOOOOOODDXXXXXXXXXXXXXSSHSSHMMHHHMMM
BBBBBBBBGGLGGGGGSSSSSSZZCCCCCCCCCCCCCCZZZZZZZZZZZMMMMMMMMMMMMMMMMZZZZZZZZZZZZZZZAYAAAAATBBBBBBBBBIIIZOOZZZZOODDDDDXXXXDXXXXXXXSSHSHHMMHHMMMM
BBBBBBBBGGGGGGAASSSSSSSSCCCCCCCCCCCCCCZZZZZZZZZZZMMMMMMMMMMMMMMMZZZZZZZZZZZZZZZAAAAAAAATTBBBBBBBBZIZZZZZZZZOODDDDDDDDDDDQQQXXSSSHHHHHHHHMMMM
BBBBBBBBBGGGFFSSSSSSSSCCCCCCCCCCCCCWCCCZZZZZZZZZZZZCMMMMMMMMMMMMZZZZZZZZZZZZZTZAAAAAAAAAAQQBBBBBZZZZZZZZZZZOOODDDDDDDDDQQQQXXSHHHHHHHHHHHYYM
BBBBBBBBBBBBBSSSSSSSSSCCCCCCCCCCCCCWCCCZZZZZZZZZZZZMMMMMMMMMMMMMZZZZZZZZZZZTTTZAAAAAAAAAAQQBBBBBZZZZZZZZZZZZDODDDDDDDDDQQQQQXXHHHHHHHHHHHLYY
BBBBBBBBBBBBBBSSSSSSSSCCCCCCCCCCCCWWCCZZZZZZZZZZZZZYMMMMMMMMMMYZZZZZZZZZZZTTTTTWBAAAAAAAQQQBBBBBWZZZZZZZZZZZDDDDDDDDDDDQQQQQQHHHHHHHHHHHHYYY
BBBBBBBBBBBBSSSSSSSSSSSCCCNNCCCWWWWWYYYZZZZZZZZZZYYYYYMMMKMKMMMKKZZZZZZZZZTTTTXBBBAAAAAAQQQBBBBBBZZZZZZZZZSZDDDDDDDDDDDQQQQQQQHHHHHHHHHHHYYY
EEBBBBBBBBBBSSSSSSSSSSSCCNNCCCZWWZWYYYYYYYZZZZZZZYYYYAMMMKKKMMKKKZZZZZZZZZKKKBBBBBVBAIAQQQQBBBOOZZZZZZZZZZZYDDDDDDDDDDDQQQQQQQHHHHHYHHHHYYYY
EEBBBBBBBBBBSSSSSSSSSSSSCNNCGCZZZZZZYYYYYYZZZZZZZYYYYAAMMKKKKKKKKKZZZZZZZZKZKBBBBBBBBBQQQQQQQBBBBZZXZZZZZZDDDDDDDDDDQDDDQQQQQQBHHHHYYHHHYYYY
EEBBBBBBBBBBSBBSSSSSSSSSSSNNZZZZZZZZYYYYYYYYZZXXYYYYAAAAMKKKKKKKNNNZZZZZZZZZBBBBBBBBJJJQQQQQQQXZZZZXZZZZZZFFFFDDDDDDQDDDDQQQBBBBYYYYHHYYYYYY
EEEBEEBBBBBBBBSSSSSSSSSJJJJJZZZZZZZYYYYYYYYYAXXXYYYYAAAEEKKKKKNKNNNNNZZNZZTBBBBBBBBBJJBQQQQQQQXXXXXXXXXZZFFFFDDDDDQDQDDDDQQQQQBBBYYYYYYYYYYY
EEEEEEBBBBBBBBBSSSSSJCSJJJJPZZZZZZZYYYYYYYXXXXXXXYYYXXDEEEEKKNNNNNNNNNNNNBBBBBBBBBBBBJBSOQQQVQXXXXXJJXXJZFFQQQQQDQQQQQDQQQQQQBBBYYYYYYYYYYYY
EEEEEEZEBBOOBBBSSSJBJCCJJJJJZZZZZZZYYYYYYXXXXXXXXXYXXXXEEEEKKNNNNNNNNNNNNNNBBBBBBBBBBBBOOOQQVXXXXJJJJJJJJFQQQQQQQQQQQQQQQQQQBBBBYYBYYYYYYYYY
EEEEEEZEOBOOBOBSSOJJJJJJJJJJJZZZZZZZCCCAAAAXXAAXXXXXXEEEEEEKKNNNNNNNNNNNNNNBBBBBCBBBBOOOOOQXXXXXYJJJJJJJJJQQQQQQQQYYQQQQQQQQBBBBBBBBBBYYYYYY
EEEEEEEEOOOOOOBOOOJJJJJJJJJJJTZZZZCCCCCCCAAAAAKXXOXOEEEEEEEKKNNNNNNNNNNNNNNNBBBCCCCOOOOOOWYYYYYYYJDDJJJJJJWQQQQQQQYYQQQQQQBBBBBBBBBBBBYYYYYY
EEEEEEEEOOOOOOOOOJJJJJJJJJJJJJJJFGCCCCCCCCCAKKKQXOOOEEEEEEEKKNNNNNNNNNNNNNNNNBCCCCCOOOOOOOYYYYYDDDDDJJJJJJWWQQQQYYYYYYQQQQBBBBBBBBBBRBYYYYYY
EEEEIEOOOOOOOOOOOJJJJJJJJJJJJJZZGGGGCCCCCCCKKKKKKOOEEEEEEEEEECCNNNNNNNNNNNNNNCCCCCOOOOOOOYYYYYYDDDVDDDJJJJWWQQQJYYYYYMMMMMMMMMMJJJJJRBYYYYYK
EEEIIROOOOOOOOOOJJJJJJJJJJJJJJJZGGGGZZCCUUKKKKKKKKOOHPPEEEEEECCNNNNNNNNNNNNNCCCCCCOOOOOOYYYYYYYYDVVVDAJAWWWWQQQDYYYYYMMMMMMMMMMDJJJJJOYKYKKK
ERRRRRRROOOOOOOOOJJJJJJJJJJJJJJZZGZZZCCCUUUKKKKKKKOOHHHPEECCCCCCNNNNNNNNNNNNCCCCYCOYYOOOYYYYYYDDDDVVDAAAAWWQQWDDYYYYYMMMMMMMMMMJJJJJJJYKKKKK
ERRRRRRRRROOOOOOOOJJJJJJJJJJJJJZZZZZZZZZZUUUUKKKIIIIFHPPPECCCKKCNNNNNNNNNNCCCCYYYYYYYOYYYYUUYYYDDDDDAAAAAWWWQWDDDYYYMMMMMMMMMMMJJJJJNYYKKKKK
RRRRRRRRRROOOOOOOOOJJJJJJJJJJJJZZZZZZZZZUUUUUUKGGGIIHHHHPKKCKKKKNCCNNNNCCNNNCCCCYYYYYYYYYYUUUTADDAAAAAAWWWWWWWWWDDDOMMMMMMMMMMMJJJJJJLLLKKKK
RRRRRRRORROOOOOOSOOJJJJJJJJJJVZZZZZZZZZZUUUUUUKGGIIIHHHHPKKKKKKKKKCCCCCCCCNCCCCCCCCCHYHHYUUUUAAADAAAAAAAAAWWWWWDDDDOMMMMMMMMMMMJJJJJJLKKKKKK
ZZRRRRROOOOOSOOOSOOOJJJPJJJJVVVZZZZZZZUUUUUUUUUIIIIIIHHHPKKKKKKKKKKCCCCCCCCCCCCCCCCHHHHHHHUUNAAAAAAAAAAAXAWAWWWDDDDOMMMMMMMMMMMJJJJJJJJKKKKK
SZRXXROOSSOSSSSSSSOOOPJPJJJJVVVZZZXXXUUUUUUUUUUIIIIIIHHKKKKKKKKKKKKCCCCCCCCCCJCCCHHHHHHHHHUUNAAAAAAAAAAAAAAAAAWDDDDOMMMMMMMMMMMJJJJJJJKKKKKK
ZZZXXZOSSSSSSSSSSSSSSPPPPJJJVZZZZZZXXVVVVUUUUUUUIIIIIHBBKKKKKKKKKKKCCCYYYCCJJJCCHHHHHHHHHHCCAAAAAAAAAAAAAADAAIWDDDDOMMMMMMMMMMMJJJJJJJKKKKKK
ZZZZZZOSSSSSSSSSSSPPPPPPPPJVVVVVVZXXXCXXVUUUUUUUIIIIIHHBBKKKKKKKKKKCCYYAYCCJJJCCHHHHHHHHHHCHRRAAAAAAAAAAAAAAAAADDDDOMMMMMMMMMMMJYJJJJJKKKKKK
ZZZZZZZSSSSSSSSSSSPPPPPPPPPPPVVVVZXXXXXXVUUUUIIIIIIIIIZZKKKKKKKKKKKKCYYYYYCJJJCCCHHHHHHHHHHHHRRAAAAAAAAAAAAAAAIIIDCCLOOMMMMMJJYYYKKYKKKKKKKK
ZZZZZZZZSSSSSSSSSSPPPPPPPPPVVVVVVVVXXXXXUUUUUIIIIIIIIIZZKKKKKKKKKKKKYYYYDDJJJJJJJIIIHHHHHHHHHRRAAAAAAAAAAAAMMLLLLLLLLOOMMMMMYYYYKKKKKKKKKKKK
ZZZZZZZZASSSSSSSJSPPPPPPPPPPVVVVVVXXXXXXXXUUUUIIIIIIIIIZZKKKKKKKEEDYYYYYYDJJJJJJJJIIJHHHHHHHHRRRRRARARRARRAAMLLLLLLLLOOOOOJYYYYYKKKKKKPKKKKK
ZZZZZZZZZZSSSSSSPPPPPPPPPPVVVVVVVVVXXXXXXXXUUUUIIIIHIIZZZZZZKKKKEEDYYYYYDDDJJJJJJJIIJJHHHHHHHRRRRRRRRRRRRRRAALLLLLLLLOOOOOJYYYYFFFKKPKPPPKWK
ZZZZZZZZZZZUSDSSSPPPPPPPPVVVVVVVVXXXXXXXXXXUUUUUUIIIIIZZVVZKKEFEEEYYYYYYDJJJJJJJJJJJJHHHHHHHHFFFRMMMMMMRRRRRLLLLLLLLLOOOOOJYFFFFFEKPPPPPPKWK
ZZZZZZZZZZZZDDDSSPPPPPOPPPPVVVVVVXXXXXXXXXXXUUKUUIIIIQVZVVVTKEEEEEEYYYYYDJJJJJJJJJLJHHHHHTHHHFFUMMMMMMMMMMRRRRLLLLLLLLOOOOOOOFFFFFFGPEEPPWWK
ZZZZZZZZZZZZZDDDSPPPPPOOEPVVVVVVVVXXXXXXXXXXUKKKKKIIIQVVVVVTTEEEEEEETTYYYJJJJJJJJJJHHHHHHHHHHFFUMMMMMMMMMMRRLLLTLLDLARAOOOOOOHHFFFXPPEEPPPPK
ZZZZZZZZZZZZDDDDDPPPPOOOOOOOOVVVVVXXXXXXXXXUUKKKKKKIQQVVKVTTTEEEEEEETTTTJJJJJJJJJJZZHHHHHHHHFFFMMMMMMMMMMMMRJTTTTTAAAAAOOOOOOOHFFFFFPPPPAPPA
ZZZZZZZZZZZZDDDDDPPPPOOOOOOOOVVVVXXXXXXXXXUUKKKKKKKIIKKAVVVVTTEEEEEETTTTTTJJJJJJJJZZZHHHHHFFFXXXXXXXXXMMMMMJJTTTTTTAAAAAAOOOOOHFFFFFPPPAAAAA
ZZZZZZZZZZZIZDDDDDDPPOOOOOOOOVVVVBXXXXXXXPKKKKKKKKKKKKAAVTTTTTTTEEEETTTUUUUUUJJJJJJZZHHHHHFFFXXXXXXXXXXXXXXXJJJTTTTAAAAAAOOHOOHFFFMPPPSPPPAA
BZZZZZZZZZZZZZDDDDDPDOOOOOOOOOOVVBLXXXXTXXKKKKKKKKKKKKKKTTTTTTTTTEEETTUUUUUUFJJJJJJJHHYHHHHFXXXXXXXXXXXXXXXXJJTTTTTAAAAAAOAHHHHHPFFPPPPPPPAA
BZZZZZZZZZZZZZDDDDDDDDOOOOOOOBBBBBLXXXXKKKKKKKKKKKKKKKKKTZZTTTTTTEEETUUUUUUUJJJJJJCCCCFFHHFFXXXXXXXXXXXXXXXXJTTTJTTAAAAAAAAAAAAPPPPPPPPPPPAA
BZBBBZWWZZNZDZDDDDDDDDDDOOOOOLLBBBLLXXXXRRRRKKKKKKKKKKKKTZZTTTTTTTTTTUUUUUUUUJJJJJCCCCFFFFFFXXXXXXXXXXXXXXXXTTTTJTTAAAAAAAAAADPPPPPPPPPPPPPA
BBBBBBBBBWWNDDDDDDDDDDDDODDOOLLLLLLXXXXRRRRNNNNNKKKKKAAZZZZTTTTTTTTUUUUUUUUCCCJJJVVVFFFFFIIIXXXXXXXXXXXXXXXXJTTTJJTAAAAAAAAAAPPPPPPPPPPPAAAA
BBBBBBBBWWNNDDDDDDDDDDDDDDDDDDLLLLLLXRRRRRRNNNNNKKKKKKZZZZZZTTTTTTTUUUUUUUKKVCCJJVVVCFFFFFIIXXXXXXXXXXXXXXXXTTJJJJTAAAAAAAAAAAPPPPPPPPPPPPAA
BBBBBBBWWWNNDNDDNDDDDDDDDLLLLLLLLLLLLRRRRRRNNNNNKKKKKZZZZZZZTTTTKKTKAUUUUKKKKCCCJVVVCCFFCFIIXXXXXXXXXXXXXXXXTTJJJJTTTAAAAAAAAAZPPPPPPPPPPPAA
BBBBBBBRWWNNNNNNNNDDDDDDLLLLLLLLLLLLLLRRRRRNNNNNKKKZZZZZZZZZZNNNNKKKUBUUUKKKKCVVVVVVCCCFCCCIXXXXXXXXXXXXXXXXTTTJJKTTTAAAAAAAAAZZPPPPPPPPPPPA
BBBBBBBBBNNNNNNNNDDDDLLLLLLLLLLLLLLLLLRRRRRNNNNNKZZZZZZZZZZZZNNNKKKKUUUUUKKKKCVVVVVVCCCCCCCIXXXXXXXXXXZZZZKKKKKJJKKTTTTAAAAEAAZZZZPZPPPPPPPA
BBBBBBBVNNNNNNNNNDDDDDDLWWLLLLLLLLLLRRRRRRRNNNNNZZZZZZZZZZZZZNNNNKKKUUKUKKKKKCVVVVVVCCCCCCIIIIIIZZZZZZZZZZKKKKKKKKKTTTTTAAAEAZZZZZZZZZPPIITA
BBBBBBBBBLNNNNNNNDDDDKKWWWLLLLLLLLLLLRRRNNNNNNNNNNZZZZZZZZNZNNKNNLKKUKKKKKKKKCVVVVVVCCCCCCCVILIIZZZZZZZZZZKKKKKKKKKKKTTTAAAEEGGZZDDDDZPPITTA
BBBBBBBBBLLLNNNNNNDKKKKKWWWWWLLLLLLLRRRRNNNNNNNNNNNNZZZZZNNNNKKKKKKKKKKKKKKKKKVVVVVVKCCCCCCCLLLIZZZZZZZZZZKKKKKKKKYYTTTTTAEEGGGZDDDDTZZZTTTT
BBBBBBBBLLLLNNNNNNKKKKKKWWWWLLLLLLLLRRRRNNNNNNNNNNNNZZZZZZNNNNKKKKKKKKKKKKKKKKVVVVVVVVVVCCCCCCLLIITZZZZZZZKKKKKKKKYYYYTTTGGGGGGDDDDDTTTTTTTT
BBBBBBOWLWLLLNNNKNKKKKKKWWWWLLLLLLLLLRRRNNNNNNNNNNNNZZZZZZNNNNKKKKKKKKKKKKKKKKVVVVVVVVVVKKCQQFLLLTTZZZZZZZKKKKKKYYYYYTTTGGGGGWWWDDDDDDTHTTTT
BBBBBLWWWWWNNNNNKNKKKKKWWWWLLLLLLLWLLRRRNNNNNNNNNNNNZZZZZZZNNNNKKKDWWWKKKKKKKRVVVVVVVVVVKKVQQFFFFCCZZZZZZZKKKKKYYYYYTTTTGGGGGGWDDDDDDDTTDLTT
BBBBBBWWWWWNCNNNKKKKKKKKWWWWLWLWLLWLLRRRNNNNNNNNNNNNZZZZZZZNNNNNKKDWWWKKKKKRRRRRRQVVVVVVKKKQQFQFFFCZZZZKKKKKKKKKKYYYYTTTGGGGGGGDVDDDDDDDDDDD
BBBBBBBBWWWCCKKKKKKKKKKKWWWWWWWWLWWWRRRRNNNNNNNNNNNNZZZZZZZNNNNNOWWWWWKKKRRRRRRRRRKKKKKKKKKQQQQQCCCCCCKKKKKKRKKKRYYYYTGTGGGYWDDDDDDDDDDDDDDD
BBBBBBBBHWWHKKKKKKKKKKKKKWWWWWWWWWWWRRRRRNNNNNNNNNNNEEEEZZNNONNNOOOWWWKKKKRRRRRRRRKKKKKFKKKQQQQQKCCWWCKKKKKRRRRRRJXXXTGGGGGYYDDDDDDDDDDDDDDD
FBBBBBHHHHHHKKKKKKKKKKKKKWWWWWWWWWWWWRRRRNNNNNNNNNNNEEEEZZNNOOOOOOOWOWKKKRRRRRRRKKKKKKKFFFFQQQQQQWWWCCCKKKRRRRRRRXXXXXGGGGYYODYYDYYDDDDDDDDD
BBBBBBBBHHHHHKKKKKKKKKKKKWKWWWWWWWWWWWRRRNNNNNNNNNNNOOEEEZNNNOOOOOOOOWWUKKCCRRRRKKKKKKKKQQQQQQQQWWWWCCCCCKRRRRRRXXJJJYYGGYYYYYYYYYYYYDDDDDDD
BBCBOBECCCHHKKKKKKKKKKKKKKKWWWWWWWWWWWRRRRRRRRRROOOOOOEEEZZNSOOOOOOOOUUUCCCCRRRIIIKKKKKKQQQQQQQQQQCWWCCCCRRRRRRRXXIYYYYGGYYYYYYYYYYYYYYYYYDD
CCCCCCCCCCCKKKKKKOKKKKKKKKKWWWWWWWWWWWRRRRRRRRROOOOOEEEEEZZSSOOOOOOUUUUCCCCCCCIIIKZKKKKKKKQQQQQQQQCCCCCCWWWWRRRXXXIYYYYYGYYYYYYYYYYYYYYYYYDD
CCCCCCCCCCKKKKKKGGGGKKKKKKKWWWWWWWWWWWRRRRRRRRROOOOOEEESSSZSSOMMOOOOCCCCCCCCCIIIIKKKKKKKKIQQQQQPPQQQCCCCCWWRRRXXXIIIYYYYYYYYYYYYYYYYYYYYDDDD
CCCCCCCCCCCKKKKKGGGGKKKKKKWWWWWWWWEWWRRRRRRRRRRROOOOOOSSSSSSSMMOOOOOOCXCCCCCCIISSSLLLKKKIIQIIIICCCCCCCCCCWWRRRXXXIIYYYYYYYYYYYYYYYYYYYYYDDDD
CCCCCCCCCCCCCKKGGGGGGGKKKKWKWWWEWWEEEGGRRRRRRRUOOOOOOOSSSTSSSMMOOOOOOOOOCCCCCIISSSSLLKKIIIIIIIIICCCCCCCCCCCXXXXXXXIIYYYYYYYYYYYYYYYYYYYDDDDD
CCCCCCCCCCCCCCTGGGGGGGGGKKKKEEWEEEEEEGPRPPPRRUUOOOOOOOSSSTSSSMOOOOOOOOOOOCCCCIIISSSSSIIIIIIIICCCCCCCCCCCCCCXJXXXIIIIIYYYYYYYYYYYYCCYYYYDDDDD
CCCCCCCCCCCCGTTGGGGGGGGGKKEEEEEEEEEEEPPPPPPRUUOOOOOOOOOOSOSSSOOOOOOOOOOOOOIICCISSSSSIIIIIIIIICICCCCCCCCCCCCJJJXXIIIIIIIYYYYYYYYYCCCYYYDDDDDD
CCCCCCCCCCCGGGGGGGGGGGGGKKEEEEEEEEEEEEEPPPPRUUOZOOOOOOOOSOSSSOOOOOOOOOOOOOOIIIISSSUSIIIIIIIIIIICCCCCCCCCCCJJJJJJIIIIIIIYYYYYYYYYCCYYYYYDDDDD
CCCCCCCCCCCCGGGGGGGGGGGGKKKEEEEEBEEEEPPPPPPPPOOOOOOOOOOOOOOUOOOOOOOOOOOOOOOOIIIIVVIIIIIIIIIIIIIIICICCCCCCCCJJYYJYIIIIIIYYYYYYYYYYYYYYYDDDDDD
CCCCCCCCCCCCGGGGGGGGGGGGGKKKEEEEEEEEEPPPPPPPPOOOOOOOOOOOOOOUOOOOOOOOOOOOOOOOOOIIIIIIIIIIIIIIIIIIIIICCCCCCCCYYYYYYIIIIIIIYYYYYYYYYYYYYDDDDDDD
CCCCCCCCCCCCGGGGGGGGGGGGGKKKKKKKEEEECPPPPPPPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOIIIIIIIIIIIIIIIIIIIIICIICCCCCYYYYYYYYYYYYYYYYYYYYYYYYYYYDDDDDD
CCCCCCCCCCCGGGGGGGGGGGGGGKKKKKKKEEECCCCPPPPIOOOOOOOOOOOOOOPOOOOOOOOOOOOOOOOOGGGGIITIIIIIIIIIIIIIIIIIIICCCYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYDDY"""

class Node:
    plant: str
    left: 'Node'
    top: 'Node'
    right: 'Node'
    bottom: 'Node'
    visited: bool

    def __init__(self, plant: str, left: 'Node', top: 'Node', right: 'Node', bottom: 'Node'):
        self.plant = plant
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.visited = False

    def __str__(self):
        return f"|{self.plant}|"

plants_rows = input.split("\n")
#init empty node matrix
node_matrix = [[Node("", None, None, None, None) for _ in range(len(plants_rows[0]))] for _ in range(len(plants_rows))]
for i in range(len(plants_rows)):
    for j in range(len(plants_rows[i])):
        current_node = node_matrix[i][j]
        top = None
        left = None
        if i != 0:
            top = node_matrix[i-1][j]
            top.bottom = current_node
        if j != 0:
            left = node_matrix[i][j-1]
            left.right = current_node
        current_node.plant = plants_rows[i][j]
        current_node.top = top
        current_node.left = left
res = 0
for k in range(len(node_matrix)):
    for l in range(len(node_matrix[k])):
        current_node = node_matrix[k][l]
        if current_node.visited:
            continue
        stack = [current_node]
        current_node.visited = True
        area = 0
        perimeter = 0
        while stack:
            current_node = stack.pop()
            area += 1
            if not current_node.left or current_node.left.plant != current_node.plant:
                perimeter += 1
            elif current_node.left.plant == current_node.plant and not current_node.left.visited:
                stack.append(current_node.left)
                current_node.left.visited = True
            if not current_node.top or current_node.top.plant != current_node.plant:
                perimeter += 1
            elif current_node.top.plant == current_node.plant and not current_node.top.visited:
                stack.append(current_node.top)
                current_node.top.visited = True
            if not current_node.right or current_node.right.plant != current_node.plant:
                perimeter += 1
            elif current_node.right.plant == current_node.plant and not current_node.right.visited:
                stack.append(current_node.right)
                current_node.right.visited = True
            if not current_node.bottom or current_node.bottom.plant != current_node.plant: 
                perimeter += 1
            elif current_node.bottom.plant == current_node.plant and not current_node.bottom.visited:
                stack.append(current_node.bottom)
                current_node.bottom.visited = True
        res += area * perimeter
            

        
print(res)