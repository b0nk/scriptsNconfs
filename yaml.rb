require 'yaml'

if File.exist?('test.yml')
  @storage = YAML.load_file('test.yml')
else
  @storage = {}
end

# let's add a nick name and associate stuff to it like alt-nick, gender and age
# 
# nick: foobar
#   alt: barfoo
#   gender: F
#   age: 25

@storage['foobar'] = {
                      'alt' => 'barfoo',
                      'gender' => 'F',
                      'age' => 25
					  }

# let's add another nick
# 
# nick: bob
#   alt: boob
#   gender: M
#   age: 26

@storage['bob'] = {
                   'alt' => 'boob',
                   'gender' => 'M',
                   'age' => 26
				   }

# now let's access some data

# let's get foobar's alt nick

puts @storage['foobar']['alt']

# and now bobs age

puts @storage['bob']['age']

# lets change bobs age

@storage['bob']['age'] = 27

puts @storage['bob']['age']

# does the subkey alt exist in foobar

puts @storage['foobar'].key? 'alt'

# does the subkey realname exist in bob

puts @storage['bob'].key? 'realname'

puts @storage['bob'].key? 'zipcode'

# lets add another key to bob

@storage['bob']['zipcode'] = 54346

puts @storage['bob'].key? 'zipcode'

puts @storage['bob']['zipcode']
