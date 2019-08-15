import json
import pygal_maps_world.maps

from country_codes import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cp1, cp2, cp3 = {}, {}, {}
for c, p in cc_populations.items():
    if p < 10000000:
        cp1[c] = p
    elif p < 1000000000:
        cp2[c] = p
    else:
        cp3[c] = p

# 看看每组包含多少国家
# print(len(cp1))
# print(len(cp2))
# print(len(cp3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')
