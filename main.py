def main():
    alphabet = list('abcdefghijklmnopqrstuvwxyz'.upper())
    first_name_list = ['Blubberbutt', 'Benedict', 'Benadryl', 'Benchthis', 'Bonapart',
                       'Brokenbrick', 'Boppinstick', 'Benefit', 'Scissorkick', 'Backitup',
                       'Bezzlebub', 'Burgerking', 'Blenderdick', 'Billiardball', 'Guiltyverdict',
                       'Beanbag', 'Carrotstick', 'Brodyquest', 'Beachbody', 'Bendylick',
                       'Baseballmitt', 'Begbug', 'Bunsenburner', 'Bengaltiger', 'Budapest', 'Handpicked']
    last_name_list = ['Calldispatch', 'Comedicmispatch', 'Cunningscratch', 'Cumberfinch', 'Humperdinck',
                      'Lumbertatch', 'Flubbercrack', 'Cumberbatch', 'Bandersnatch', 'Cuttlefish',
                      'Slumblerbelch', 'Cupboardlatch', 'Combyourthatch', 'Thundermunch', 'Cricketbat',
                      'Johnnycash', 'Comelycat', 'Custardbath', 'Thundercats', 'Numbercrunch',
                      'Luckycatch', 'Covertrack', 'Uptoscratch', 'Compasstrap', 'Chunkybap', 'Candygram']
    name = input('Введите свои имя и фамилию ').strip().title()
    true_name = False
    if name.find(' ') == name.rfind(' ') != -1:
        names_list = name.split(' ')
        first_name_digit = names_list[0][0]
        last_name_digit = names_list[1][0]
        true_name = first_name_list[alphabet.index(first_name_digit)] + ' ' + last_name_list[
            alphabet.index(last_name_digit)]
    return true_name


if __name__ == '__main__':
    do = True
    while do is True:
        name = main()
        if name is not False:
            print('Your Benedict Cumberbatch name is '+name)
            do = False
