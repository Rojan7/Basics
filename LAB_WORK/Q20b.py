
graph = {
 'biratnagar' : {'itahari' : 22, 'biratchowk' : 30, 'rangeli': 25},
'itahari' : {'biratnagar' : 22, 'dharan' : 20, 'biratchowk' : 11},
'dharan' : {'itahari' : 20},
'biratchowk' : {'biratnagar' : 30, 'itahari' : 11, 'kanepokhari' :10},
'rangeli' : {'biratnagar' : 25, 'kanepokhari' : 25, 'urlabari' : 40},
'kanepokhari' : {'rangeli' : 25, 'biratchowk' : 10, 'urlabari' : 12},
'urlabari' : {'rangeli' : 40, 'kanepokhari' : 12, 'damak' : 6},
'damak' : {'urlabari' : 6}
    
}

print(graph)