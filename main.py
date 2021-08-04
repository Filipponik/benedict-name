def main():
  def get_name(name, type=False):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
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

    try:
      return last_name_list[alphabet.index(name[0])] if type else first_name_list[alphabet.index(name[0])]
    except:
      return False

  name = input('Your name in life: ').lower().strip().split()

  if len(name) != 2:
    return False
  if not get_name(name[0]) or get_name(name[1], True):
    return False

  return get_name(name[0]) + ' ' + get_name(name[1], True)


if __name__ == '__main__':
  while True:
    name = main()
    if name is not False:
      print('Your Benedict Cumberbatch name is ' + name)
      break
