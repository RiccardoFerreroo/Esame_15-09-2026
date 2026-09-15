import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.dao = DAO()
        self.G=nx.DiGraph()
        self.list_states=[]
        self.list_airports=dict()
    def get_states_min_voli(self, num_voli):
        self.list_airports = self.dao.get_all_airports(num_voli) #ottengo aereoporti validi    #  {airport_id: (out_voli, in_voli)}
        print(self.list_airports)

        stati= dict()
        for airport in self.list_airports.keys():
            result=(self.dao.get_states(airport))
            print(result)
            if  stati =={} or not stati[result[0]]  :
                stati[result[0]]=result[1]
            else:
                stati[result[0]]=(result[1])
        print(stati)

        #self.list_states = self.dao.get_states(self.list_airports) #ottengo {stati: airport_id}
        #print(self.list_states)

