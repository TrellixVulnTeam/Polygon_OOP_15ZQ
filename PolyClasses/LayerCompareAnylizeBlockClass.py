##@package LayerCompareAnylizeBlockClass
#Consist of LayerCompareAnylizeBlock class definition
from PolyClasses.BooleanOperationsBlockClass import *
from PolyClasses.LayerClass import *
from PolyClasses.GateClass import *


##This class create LayerCompareAnylizeBlock objects
#
#Compare two Layers' polygons and return Gate objs if width is less than entered
class LayerCompareAnylizeBlock(BooleanOperationsBlock):

    ##  Return array of Gate objects that was derivated from 2 layers' polygons
    #   @param self The object pointer
    #   @param First_layer Layer object
    #   @param Second_Layer Layer object
    #   @param check_width_size float
    #   @return array of Gate objects
    def get_gates_arr_with_width_check(self,First_layer,Second_Layer,check_width_size):
        polygon_arr = self.__get_polygon_arr_two_layers_intersection(First_Layer=First_layer, Second_Layer=Second_Layer)
        filtered_poly_arr = self.__get_polygon_arr_with_width_check(polygon_arr,check_width_size)
        return self.__get_Gate_arr_from_poly_arr(poly_arr=filtered_poly_arr, FirstLayer=First_layer, SecondLayer=Second_Layer)


    ##  Return array of StandardPolygon objects which are result of boolean operation AND between two layers' polygons
    #   @param self The object pointer
    #   @param First_Layer Layer object
    #   @param Second_Layer Layer object
    #   @return array of StandardPolygon objects
    def __get_polygon_arr_two_layers_intersection(self,First_Layer,Second_Layer):
        first_layer_polygon_arr = First_Layer.get_polygon_array_belong_layer()
        second_layer_polygon_arr = Second_Layer.get_polygon_array_belong_layer()
        intersection_polygon_arr = []
        for i in range(len(first_layer_polygon_arr)):
            for j in range(len(second_layer_polygon_arr)):
                result_of_intersect_two_polygons_arr = self.get_resulting_polygon_arr_from_operation_AND(first_layer_polygon_arr[i],second_layer_polygon_arr[j],First_Layer.get_DrawSpace())
                if (None != result_of_intersect_two_polygons_arr):intersection_polygon_arr.extend(result_of_intersect_two_polygons_arr)
        return intersection_polygon_arr

    ##  Return array of StandardPolygon objects that has width or height less than <width_size>
    #   @param self The object pointer
    #   @param poly_arr array of StandardPolygon objects
    #   @param width_size float
    #   @return array of StandardPolygon objects
    def __get_polygon_arr_with_width_check(self,poly_arr,width_size):
        filtered_poly_arr = []
        for i in range(len(poly_arr)):
            bounds = poly_arr[i].get_poly().bounds
            if((bounds[2]-bounds[0])<width_size) or ((bounds[3]-bounds[1])<width_size): filtered_poly_arr.append(poly_arr[i])
        return filtered_poly_arr

    ##  Return array of Gate objects from array of StandardPolygon objects
    #   @param self The object pointer
    #   @param poly_arr array of StandardPolygon objects
    #   @param First_layer Layer object
    #   @param Second_Layer Layer object
    #   @return array of Gate objects
    def __get_Gate_arr_from_poly_arr(self,poly_arr,FirstLayer = None,SecondLayer = None):
        new_derivative_layer_for_gates = Layer()
        gate_arr = []
        for i in range(len(poly_arr)):
            gate_arr.append(Gate(poly_arr[i].get_array_of_dots(),new_derivative_layer_for_gates,FirstLayer,SecondLayer))
        return gate_arr