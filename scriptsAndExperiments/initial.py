from consts import Consts
from ways import load_map_from_csv
from problems import BusProblem
from path import Path
from matplotlib import pyplot as plt
from ways.draw import plotPath, plotOrders
from ways.tools import compute_distance
import numpy as np

# Read files
roads = load_map_from_csv(Consts.getDataFilePath("israel.csv"))
prob = BusProblem.load(Consts.getDataFilePath("TLV_5.in"))

# TODO - Fix the missing parts in the following code
# Print details of a random order
order = prob.orders[np.random.choice(np.arange(len(prob.orders)))]
print("One of the orders is from junction #{} at ({}, {}) to #{} at ({}, {})".format(
    order[0], roads[order[0]].lat, -1,
    order[1], -1, -1))
print("A lower bound on the distance we need to drive for this order is: {:.2f}km".format(
    compute_distance(roads[order[0]].coordinates, roads[order[0]].coordinates) / 1000))

# Create hard coded example path
examplePath = Path(roads, [2744, 2745, 2746, 2747, 85561, 62583, 46937, 42405, 19096, 17273, 46582, 43933, 465367, 57190, 819204, 819205, 47816, 16620, 819206, 465324, 3421, 819207, 19950, 819208, 529485, 646688, 646689, 646690, 646691, 646692, 646693, 646694, 47335, 646695, 646696, 522500, 646680, 646681, 646682, 646683, 7372, 867063, 867064, 867065, 867066, 867067, 867068, 867069, 705491, 49950, 49921, 705498, 926772, 926773, 926774, 926775, 926776, 870022, 593302, 921858, 926777, 926778, 926779, 43226, 926780, 811196, 867037, 926781, 926782, 926783, 867045, 580849, 926784, 580855, 66143, 867051, 880273, 926785, 880271, 926786, 926787, 926788, 926789, 926790, 870232, 926791, 926792, 926793, 926794, 926795, 926796, 926797, 926798, 867080, 867072, 926799, 926800, 863957, 11454, 603929, 866456, 50865, 866457, 866458, 867002, 867001, 867000, 612734, 612735, 612736, 612737, 612738, 612739, 870148, 96491, 96492, 612710, 542941, 870147, 542938, 870146, 870141, 612704, 870145, 464552, 464553, 565107, 466517, 466518, 466519, 466520, 466521, 466522, 466523, 466524, 466525, 754541, 754542, 754543, 754544, 96365, 96364, 96363, 96362, 96361, 96360, 57033, 57032, 57031, 57030, 57029, 50831, 50832, 12692, 50833, 50834, 12343, 50835, 50836, 50837, 50838, 50839, 50840, 35506, 35505, 35504, 35503, 35502, 35501, 35500, 35499, 35498, 35497, 35496, 35495, 35494, 35493, 866647, 718703, 866648, 851323, 866649, 866650, 866651, 866652, 866653, 866717, 851297, 866716, 851276, 737517, 851285, 866715, 73340, 866714, 866681, 866688, 866713, 851302, 851301, 851300, 851288, 851271, 851272, 866687, 866708, 866709, 737477, 737478, 73566, 737479, 605205, 605204, 724105, 724107, 724106, 724089, 724088, 724087, 724086, 724085, 724084, 724083, 724082, 724076, 724075, 724074, 724073, 724092, 724072, 871058, 871057, 871045, 871056, 871055, 871054, 871053, 871052, 871074, 871103, 871102, 871101, 871100, 871090, 871093, 871092, 866447, 603943, 870222, 870223, 871091, 863947, 871118, 59648, 66173, 871124, 871123, 870175, 870176, 870177, 870178, 870179, 580848, 626555, 870180, 870181, 870182, 66148, 66149, 880269, 880272, 880273, 50879, 50880, 50881, 50882, 50883, 50884, 50885, 50886, 50887, 867003, 867004, 867005, 867006, 867007, 867008, 867009, 867010, 49926, 49953, 653054, 867011, 867012, 867013, 40970, 867014, 867015, 866490, 867016, 32037, 32038, 32039, 11442, 32040, 32041, 32029, 32030, 32031, 32032, 32033, 32034, 32035, 32036, 32042, 32048, 32049, 32050, 32051, 32052, 32053, 32054, 32056, 32057, 32058, 32059, 50692, 50693, 50694, 50695, 50698, 50699, 50700, 50701, 50702, 84369, 84370, 84371, 84355, 12851, 12852, 84368, 17872, 12839, 12840, 84372, 84373, 84374, 84375, 833224, 833225, 833226, 833227, 833228, 47377, 47378, 47379, 47380, 47381, 47382, 47383, 47384, 47385, 47386, 47387, 50315, 50316, 50317, 50264, 50265, 50266, 50267, 50268, 50269, 50270, 32847, 32848, 32849, 32850, 32867, 32868, 32869, 32854, 893090, 691982, 893091, 39521, 39522, 66404, 66405, 66406, 3362, 3361, 47519, 47520, 47521, 47520, 47519, 3361, 3362, 645213, 645214, 465378, 49012, 3445, 869993, 46565, 869994, 528502, 869995, 724326, 542442, 819349, 49976, 819350, 49003, 49004, 49005, 48999, 544019, 867017, 866489, 867018, 867019, 867020, 867021, 867022, 867023, 40969, 867024, 867025, 867026, 867027, 653049, 49951, 49928, 867028, 867029, 867030, 867031, 867032, 867033, 867034, 867035, 867036, 50888, 867037, 926781, 926782, 926783, 867045, 580849, 926784, 580855, 66143, 867051, 880273, 926785, 880271, 926786, 926787, 926788, 926789, 926790, 870232, 926791, 926792, 926793, 926794, 926795, 926796, 926797, 926798, 867080, 867072, 926799, 926800, 863957, 11454, 603929, 866456, 926801, 926802, 926803, 866737, 926804, 926805, 926806, 926807, 926808, 926809, 926810, 866741, 926811, 73496, 926812, 35505, 926813, 464545, 926814, 5221, 926815, 12344, 612832, 926816, 12691, 926817, 47327, 57027, 926818, 46436, 866627, 465389, 819446, 819393, 599575, 819437, 46383, 912048, 926819, 7408, 65683, 912061, 46314, 926820, 926821, 926822, 25610, 11452, 46351, 528640, 529456, 65737, 65738, 65739, 65740, 65741, 65742, 65693, 65743, 65744, 65745, 530546, 715860, 715861, 715862, 715863, 525089, 715859, 530549, 715858, 715857, 25611, 25612, 25613, 25614, 25615, 25616, 25617, 25618, 25619, 25620, 25621, 25622, 25623, 25624, 654900, 654901, 654902, 654903, 654904, 654905, 525405, 525406, 525407, 525408, 525409, 525410, 525413, 525414, 10201, 54744, 67029, 67030, 67031, 67032, 67033, 67034, 67035, 67036, 67037, 67038, 67039, 67040, 67041, 67042, 67043, 67044, 578769, 578762, 578761, 578760, 578759, 578758, 578757, 578756, 578755, 742158, 742159, 742160, 742161, 742162, 742163, 742164, 742165, 742166, 742167, 742168, 742169, 742170, 742171, 742172, 742173, 742174, 742175, 742176, 742177, 742178, 524873, 742179, 742180, 742181, 742182, 742183, 742184, 742185, 67045, 67046, 67047, 742186, 742187, 742188, 742189, 742190, 742191, 742192, 742193, 742194, 742195, 742196, 742197, 742198, 742199, 742200, 742201, 742202, 742203, 742204, 67053, 67054, 67055, 67056, 67057, 929419, 929420, 608084, 80523, 80524, 80525, 80526, 80527, 80528, 80513, 42180, 530737, 530760, 530759, 530728, 530758, 530757, 22609, 22533, 22534, 22535, 22536, 22537, 22538, 22539, 461074, 80364, 80365, 80366, 80367, 80368, 80369, 80370, 80371, 80372, 80373, 80374, 80375, 80376, 80377, 80378, 42100, 22556, 22557, 33470, 33471, 33472, 33473, 33474, 33475, 33476, 33477, 33478, 33479, 33480, 33481, 33482, 33483, 33484, 33485, 33531, 33506, 33530, 33529, 33528, 33542, 33541, 33507, 33508, 33509, 33510, 33511, 33512, 33513, 33514, 33515, 33516, 33517, 33518, 33519, 33520, 33521, 33522, 33523, 33524, 33525, 33526, 33527, 33344, 33345, 33346, 33347, 33348, 816680, 816681, 33373, 33374, 33375, 33376, 33377, 23686, 23687, 23688, 23689, 23690, 23691, 23692, 23693, 23694, 23695, 23696, 23697, 23698, 23699, 23700, 23701, 23702, 23703, 595927, 595962, 595963, 595964, 595965, 595966, 595967, 595968, 595969, 595970, 595971, 595972, 631017, 631018, 631019, 631020, 631021, 631022, 631023, 631024, 631025, 631026, 631027, 631028, 813481, 813482, 813483, 813484, 813485, 813486, 813487, 813488, 813489, 813490, 813491, 813492, 813493, 813494, 33320, 33321, 33322, 33323, 33324, 33325, 20735, 20734, 20733, 20732, 20731, 20730, 20729, 20728, 20727, 20726, 20725, 20724, 20723, 20722, 20721, 20720, 33309, 33319, 822028, 822029, 822030, 822031, 822032, 822033, 822034, 822035, 822036, 810182, 810183, 810184, 810185, 810186, 810187, 810188, 810189, 810190, 810191, 810192, 810193, 810194, 810195, 810196, 813469, 813470, 813471, 813472, 813473, 813474, 813475, 813476, 813477, 813478, 813479, 813480, 516637, 516638, 516639, 516640, 516641, 516642, 516643, 516644, 516645, 516646, 516647, 516648, 516649, 516650, 516651, 516652, 595928, 595929, 816784, 816785, 816786, 816787, 816788, 816789, 816790, 816791, 816792, 816793, 816754, 816755, 816756, 816757, 816758, 816759, 816760, 816761, 816762, 816763, 816764, 816765, 816766, 816767, 816768, 816769, 595931, 595932, 595933, 595934, 595935, 595936, 595937, 595938, 595939, 595940, 595941, 595942, 595943, 595944, 595945, 595946, 595947, 595948, 595949, 595950, 595951, 595952, 33378, 33379, 33380, 33381, 33382, 33383, 33384, 33385, 33386, 33387, 33388, 33389, 595955, 595956, 595957, 595958, 590266, 595959, 33578, 595960, 595961, 23704, 23705, 23706, 23707, 23708, 8521, 23709, 33551, 33552, 29805, 33553, 33554, 33555, 33556, 33557, 33558, 33559, 25572, 33560, 33561, 33562, 33563, 523272, 523273, 25593, 523274, 523275, 523276, 523277, 523278, 523279, 523280, 67126, 67127, 67128, 67129, 67130, 67131, 67132, 67133, 67134, 67135, 67136, 67137, 67138, 67139, 67140, 67141, 67142, 67143, 67144, 67180, 67181, 67182, 67183, 46521, 46500, 702128, 906344, 906345, 906346, 906347, 906348, 29806, 29807, 29808, 96351, 96352, 96353, 78130, 78153, 96354, 96288, 96293, 96355, 96356, 56155, 96357, 96358, 96359, 754553, 542942, 542943, 542944, 542945, 542946, 542947, 542948, 542949, 542950, 542951, 542952, 542953, 47436, 47433, 869934, 869935, 869936, 869937, 869938, 869939, 869940, 869941, 866462, 603921, 869942, 869943, 869891, 509508, 869944, 869945, 509497, 869946, 869947, 869924, 509488, 869948, 49922, 49923, 49958, 49929, 49930, 49931, 49932, 49933, 49934, 20249, 49935, 49936, 49937, 49938, 49939, 41000, 49940, 49941, 49942, 49943, 49944, 49945, 49946, 49947, 705488, 705489, 705490, 926823, 926824, 556247, 926825, 866512, 926826, 926827, 17515, 17516, 522499, 522500, 522501, 522502, 522503, 522504, 522505, 522506, 522507, 522508, 46249, 46250, 692854, 869872, 893018, 893019, 46251, 46252, 46253, 6638, 46254, 46255, 46256, 46257, 46258, 46259, 46260, 46261, 16476, 880299, 880278, 880300, 880301, 880302, 861849, 880303, 880304, 880305, 880306, 864020, 893030, 893031, 85748, 893032, 893033, 19074, 19063, 893023, 893024, 720919, 17834, 17835, 2789, 711278, 931081, 931082, 931083, 893020, 893021, 893022, 17811, 17812, 893048, 893049, 893050, 893051, 893037, 893038, 893039, 893040, 893041, 17853, 893042, 893043, 893044, 893045, 893046, 893047, 544062, 741931, 741932, 544077, 17810, 936406, 936407, 936374, 936375, 3324, 3325, 3326, 3327, 3328, 3329, 3330, 3331, 3332, 3333, 35191, 35192, 35193, 35194, 35195, 35230, 35231, 35232, 35233, 35234, 35235, 35227, 705712, 831914, 831915, 831916, 831917, 831918, 831919, 826832, 826835, 699045, 546953, 546954, 546955, 35402, 546956, 546957, 546958, 546959, 546960, 534808, 534809, 534810, 534811, 534812, 534813, 534814, 534815, 534816, 534817, 534818, 534819, 534820, 534821, 534822, 534823, 534824, 534825, 534826, 546980, 546981, 546982, 546983, 546984, 546985, 546986, 546987, 546988, 546989, 546990, 890626, 890627, 890628, 890629, 815067, 725581, 710786, 725586, 715774, 816462, 882176, 882177, 882178, 57399, 57463, 57464, 57465, 57466, 57467, 882175, 882174, 882181, 563902, 563697, 750181, 750182, 563995, 726443, 57444, 566062, 866421, 866422, 866423, 866418, 564022, 866424, 866425, 866426, 866431, 866432, 866435, 822264, 822265, 866436, 866437, 866438, 533411, 533456, 35837, 35838, 617934, 899660, 533440, 912243, 854085, 854086, 30096, 30097, 31814, 31815, 31816, 31817, 31818, 31819, 31820, 31821, 31822, 31823, 31824, 31825, 31826, 31827, 31828, 31829, 533395, 533396, 533397, 533398, 36264, 36265, 608284, 608285, 608286, 608287, 533359, 533360, 533361, 533362, 533363, 533364, 533365, 533366, 533367, 533368, 533369, 31813, 533370, 533371, 703425, 703426, 703427, 703405, 703428, 30112, 31081, 31082, 31083, 703413, 31162, 31163, 31164, 30104, 31165, 31166, 31200, 533383, 533384, 533385, 533386, 533387, 533388, 533389, 533390, 533391, 533392, 533393, 533394, 703420, 703421, 703422, 703423, 703424, 703414, 703415, 703416, 703417, 703418, 703419, 854089, 854090, 854091, 854092, 854093, 854094, 31837, 31838, 31839, 31840, 531413, 531414, 531415, 531416, 531417, 531418, 531419, 531420, 531421, 531422, 531423, 531424, 531425, 942897, 942898, 942899, 942900, 942901, 942902, 531283, 531284, 531285, 531286, 531287, 531288, 531289, 531290, 531291, 531292, 531293, 531294, 531295, 531296, 531297, 531298, 531299, 531300, 531301, 531302, 854102, 854103, 854104, 854105, 854106, 854107, 854108, 854109, 854110, 854111, 854112, 854113, 854114, 854115, 854116, 854117, 854118, 854119, 854120, 854121, 854122, 854123, 854124, 854125, 532541, 532542, 532543, 532544, 532545, 532546, 532547, 532548, 532549, 532550, 532551, 532552, 532553, 532554, 532555, 532556, 532557, 532558, 532559, 532560, 532561, 532562, 532563, 532564, 532565, 532566, 97071, 97072, 97073, 97074, 606425, 606429, 606430, 606431, 606432, 606433, 606434, 820994, 820995, 820996, 820997, 820998, 820999, 821000, 821001, 821002, 821003, 821004, 821005, 821006, 821007, 820984, 820985, 820986, 820987, 820988, 820989, 820990, 820991, 820992, 820993, 821034, 821035, 821036, 737560, 723902, 36275, 723897, 723903, 723904, 696490, 696491, 696492, 696493, 696494, 696495, 696496, 696497, 606464, 606465, 606472, 97069, 97070, 740240, 740241, 740242, 740243, 740244, 740245, 740246, 740247, 740248, 740249, 740250, 740251, 740252, 740253, 740254, 740255, 740256, 740257, 740258, 740259, 740260, 740261, 740262, 740263, 740264, 2942, 2943, 2944, 2945, 2946, 2947, 2948, 2949, 2950, 2951, 2952, 36266, 36267, 36268, 36269, 36270, 727048, 727049, 727050, 727051, 727052, 727053, 727054, 727055, 727056, 727057, 727058, 727059, 727060, 727061, 727062, 531360, 727063, 727064, 531337, 727065, 727066, 727067, 727068, 727069, 727070, 727071, 31811, 31812, 31813, 533370, 533371, 703425, 703426, 703427, 703405, 703428, 30112, 31081, 703429, 703430, 703431, 533382, 703432, 703433, 703434, 703435, 703436, 727075, 533441, 727076, 727077, 727078, 727079, 727080, 727081, 866440, 866441, 866442, 68315, 68316, 68317, 68318, 68319, 68320, 533541, 533542, 533543, 533544, 533545, 30634, 30635, 30636, 30637, 57394, 866394, 816461, 866395, 866396, 585642, 866397, 724118, 724224, 724223, 724222, 724225, 724226, 585635, 724227, 864088, 866402, 724218, 724221, 546936, 585633, 724128, 724228, 724229, 724230, 699034, 724113, 68369, 724114, 588427, 727039, 727040, 727036, 727035, 727020, 727021, 568004, 864047, 727019, 727018, 727017, 727016, 727015, 727014, 588429, 568010, 727013, 727012, 534835, 727028, 727029, 727030, 727022, 727031, 35413, 35414, 35415, 35416, 35417, 890659, 890660, 513554, 34964, 890662, 818105, 818104, 35428, 35429, 35430, 35431, 35432, 35433, 35434, 35435, 35436, 35437, 846847, 846848, 846849, 846820, 846821, 846822, 846823, 846824, 846825, 846826, 846827, 846828, 846829, 846830, 846814, 846831, 846832, 846815, 513525, 56356, 513526, 513527, 513528, 513529, 513530, 513531, 513532, 513533, 513534, 513535, 2821, 2822, 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840, 2841, 2842, 2843, 2844, 2845, 944576, 3311, 944577, 846453, 640480, 846454, 846455, 640485, 846456, 572770, 846457, 846458, 846459, 711264, 85762, 944595, 640469, 846449, 846450, 846451, 846452, 880292, 85764, 880293, 880294, 712626, 880295, 880296, 880297, 864021, 44111, 44110, 44131, 944568, 893115, 900025, 881184, 820608, 944569, 880274, 944570, 16476, 881575, 881576, 861880, 881577, 881578, 881579, 46237, 46238, 46239, 46240, 46241, 32067, 46242, 46243, 46244, 46245, 46246, 46247, 46248, 869839, 869849, 893055, 893056, 646684, 893057, 646674, 522508, 529478, 529479, 529480, 529481, 529482, 529483, 529484, 529485, 6649, 46570, 899752, 899753, 40962, 40954, 471686, 528478, 528479, 528480, 528481, 528474, 528475, 528476, 528477, 528482, 528483, 528484, 528498, 528499, 528500, 528501, 724344, 866496, 866497, 866498, 866499, 49973, 49974, 49975, 49976, 819350, 49003, 49004, 49005, 48999, 11440, 11441, 11442, 32040, 32041, 32029, 32030, 32031, 32032, 32033, 32034, 32035, 32036, 32042, 32048, 32049, 32050, 32051, 32052, 32053, 32054, 32056, 32057, 32058, 32059, 50692, 50693, 50694, 50695, 50698, 50699, 50700, 50701, 50702, 50703, 50704, 50705, 50706, 24196, 50707, 50708, 50709, 50710, 50711, 50712, 73303, 73304, 73298, 73299, 73300, 14245, 73301, 73302, 834596, 834597, 834598, 59132, 834599, 834600, 834601, 834602, 834603, 834604, 834605, 834606, 834607, 834608, 834609, 10876, 10877, 10845, 10846, 10847, 10848, 10849, 10850, 10851, 10852, 10865, 10866, 97261, 97262, 97263, 97196, 97264, 97265, 97266, 97267, 97268, 97269, 97270, 97271, 97247, 97249, 617117, 97287, 97288, 97289, 72317, 72318, 72319, 72320, 72321, 72322, 72323, 72324, 72325, 72326, 72327, 72328, 72329, 72330, 68505, 68506, 68507, 68508, 68509, 68500, 68510, 68511, 68512, 68450, 68513, 68514, 68459, 617116, 617115, 69265, 68711, 617114, 617113, 68713, 617112, 617111, 617110, 617109, 68593, 68592, 68591, 68590, 68589, 68588, 68587, 68586, 68585, 68584, 68583, 68582, 68581, 68464, 68465, 68466, 68467, 20186, 20187, 20188, 20189, 20172, 28144, 28145, 28146, 28147, 28148, 28149, 28150, 28151, 28152, 28153, 28154, 20107, 29247, 29248, 29249])

# Plot the orders
plotOrders(roads, prob.orders)
plt.title("Showing orders. Click to show path")
plt.show(block=False)
plt.waitforbuttonpress()

# Plot the path
plotPath(examplePath)
plt.title("Showing path")
plt.show()

# TODO : Print the path's length/distance in kilometers.
print("Path length: {:.2f}km".format(-1))


