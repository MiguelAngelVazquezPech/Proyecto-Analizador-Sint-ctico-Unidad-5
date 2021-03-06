
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightIFELSEleftSEMIleftCOMMAleftASIGNARleftSEMIleftNEleftLTLEGTGEASleftMASMENOSleftMULTIDIVIDEleftLBRACERBRACEleftPARENTESISIZQPARENTESISDERAS ASIGNAR BOOL BREAK COMMA DECIMAL DIVIDE DOUBLE ELSE FALSE FIN FOR GE GT ID IF INICIO INT LBRACE LE LT MAS MENOS MULTI NE NULL NUMERO PARENTESISDER PARENTESISIZQ PRINT RBRACE SEMI STRING TRUE VAR VOIDdeclaracion : IF PARENTESISIZQ expresion GT expresion PARENTESISDER LBRACE expresion SEMI RBRACEdeclaracion : ELSE LBRACE expresion SEMI RBRACEdeclaracion : INT expresion ASIGNAR expresion SEMIdeclaracion : DOUBLE expresion ASIGNAR expresion SEMIdeclaracion : INICIOdeclaracion :  FINdeclaracion : expresion SEMI\n    expresion  :    expresion MAS expresion \n                |   expresion MENOS expresion \n                |   expresion MULTI expresion\n                |   expresion DIVIDE expresion \n\n    expresion : MENOS expresion %prec MENOS\n    expresion  : PARENTESISIZQ expresion PARENTESISDER \n                | LBRACE expresion RBRACE\n\n    \n    expresion   :  expresion LT expresion \n                |  expresion GT expresion \n                |  expresion LE expresion \n                |   expresion GE expresion \n                |   expresion ASIGNAR expresion \n                |   expresion AS expresion\n                |  PARENTESISIZQ expresion LT expresion PARENTESISDER\n                |  PARENTESISIZQ expresion GT expresion PARENTESISDER\n                |  PARENTESISIZQ expresion LE expresion PARENTESISDER\n                |  PARENTESISIZQ expresion GE expresion PARENTESISDER\n                |  PARENTESISIZQ expresion ASIGNAR expresion PARENTESISDER\n                |  PARENTESISIZQ expresion AS expresion PARENTESISDER\n    expresion : DECIMALexpresion : NUMEROexpresion : ID'
    
_lr_action_items = {'IF':([0,],[2,]),'ELSE':([0,],[6,]),'INT':([0,],[7,]),'DOUBLE':([0,],[8,]),'INICIO':([0,],[9,]),'FIN':([0,],[10,]),'MENOS':([0,3,4,5,7,8,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,76,77,],[11,11,19,11,11,11,11,-27,-28,-29,11,19,11,11,11,11,11,11,11,11,11,11,19,11,19,19,-12,19,-13,11,11,11,11,11,11,-8,-9,-10,-11,19,19,19,19,19,19,-14,19,11,11,11,19,19,19,19,19,19,19,19,19,-21,-22,-23,-24,-25,-26,11,19,]),'PARENTESISIZQ':([0,2,3,5,7,8,11,15,18,19,20,21,22,23,24,25,26,27,29,35,36,37,38,39,40,53,54,55,76,],[3,15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'LBRACE':([0,3,5,6,7,8,11,15,18,19,20,21,22,23,24,25,26,27,29,35,36,37,38,39,40,53,54,55,75,76,],[5,5,5,29,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,76,5,]),'DECIMAL':([0,3,5,7,8,11,15,18,19,20,21,22,23,24,25,26,27,29,35,36,37,38,39,40,53,54,55,76,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'NUMERO':([0,3,5,7,8,11,15,18,19,20,21,22,23,24,25,26,27,29,35,36,37,38,39,40,53,54,55,76,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'ID':([0,3,5,7,8,11,15,18,19,20,21,22,23,24,25,26,27,29,35,36,37,38,39,40,53,54,55,76,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'$end':([1,9,10,17,72,73,74,79,],[0,-5,-6,-7,-2,-3,-4,-1,]),'SEMI':([4,12,13,14,32,34,41,42,43,44,45,46,47,48,49,50,51,52,63,64,66,67,68,69,70,71,77,],[17,-27,-28,-29,-12,-13,-8,-9,-10,-11,-15,-16,-17,-18,-19,-20,-14,62,73,74,-21,-22,-23,-24,-25,-26,78,]),'MAS':([4,12,13,14,16,28,30,31,32,33,34,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,77,],[18,-27,-28,-29,18,18,18,18,-12,18,-13,-8,-9,-10,-11,18,18,18,18,18,18,-14,18,18,18,18,18,18,18,18,18,18,-21,-22,-23,-24,-25,-26,18,]),'MULTI':([4,12,13,14,16,28,30,31,32,33,34,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,77,],[20,-27,-28,-29,20,20,20,20,20,20,-13,20,20,-10,-11,20,20,20,20,20,20,-14,20,20,20,20,20,20,20,20,20,20,-21,-22,-23,-24,-25,-26,20,]),'DIVIDE':([4,12,13,14,16,28,30,31,32,33,34,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,77,],[21,-27,-28,-29,21,21,21,21,21,21,-13,21,21,-10,-11,21,21,21,21,21,21,-14,21,21,21,21,21,21,21,21,21,21,-21,-22,-23,-24,-25,-26,21,]),'LT':([4,12,13,14,16,28,30,31,32,33,34,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,77,],[22,-27,-28,-29,35,22,22,22,-12,22,-13,-8,-9,-10,-11,-15,-16,-17,-18,22,-20,-14,22,-15,-16,-17,-18,22,-20,22,22,-16,-21,-22,-23,-24,-25,-26,22,]),'GT':([4,12,13,14,16,28,30,31,32,33,34,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,77,],[23,-27,-28,-29,36,23,23,23,-12,55,-13,-8,-9,-10,-11,-15,-16,-17,-18,23,-20,-14,23,-15,-16,-17,-18,23,-20,23,23,-16,-21,-22,-23,-24,-25,-26,23,]),'LE':([4,12,13,14,16,28,30,31,32,33,34,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,77,],[24,-27,-28,-29,37,24,24,24,-12,24,-13,-8,-9,-10,-11,-15,-16,-17,-18,24,-20,-14,24,-15,-16,-17,-18,24,-20,24,24,-16,-21,-22,-23,-24,-25,-26,24,]),'GE':([4,12,13,14,16,28,30,31,32,33,34,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,77,],[25,-27,-28,-29,38,25,25,25,-12,25,-13,-8,-9,-10,-11,-15,-16,-17,-18,25,-20,-14,25,-15,-16,-17,-18,25,-20,25,25,-16,-21,-22,-23,-24,-25,-26,25,]),'ASIGNAR':([4,12,13,14,16,28,30,31,32,33,34,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,77,],[26,-27,-28,-29,39,26,53,54,-12,26,-13,-8,-9,-10,-11,-15,-16,-17,-18,-19,-20,-14,26,-15,-16,-17,-18,-19,-20,-19,-19,-16,-21,-22,-23,-24,-25,-26,26,]),'AS':([4,12,13,14,16,28,30,31,32,33,34,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,77,],[27,-27,-28,-29,40,27,27,27,-12,27,-13,-8,-9,-10,-11,-15,-16,-17,-18,27,-20,-14,27,-15,-16,-17,-18,27,-20,27,27,-16,-21,-22,-23,-24,-25,-26,27,]),'PARENTESISDER':([12,13,14,16,32,34,41,42,43,44,45,46,47,48,49,50,51,56,57,58,59,60,61,65,66,67,68,69,70,71,],[-27,-28,-29,34,-12,-13,-8,-9,-10,-11,-15,-16,-17,-18,-19,-20,-14,66,67,68,69,70,71,75,-21,-22,-23,-24,-25,-26,]),'RBRACE':([12,13,14,28,32,34,41,42,43,44,45,46,47,48,49,50,51,62,66,67,68,69,70,71,78,],[-27,-28,-29,51,-12,-13,-8,-9,-10,-11,-15,-16,-17,-18,-19,-20,-14,72,-21,-22,-23,-24,-25,-26,79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,3,5,7,8,11,15,18,19,20,21,22,23,24,25,26,27,29,35,36,37,38,39,40,53,54,55,76,],[4,16,28,30,31,32,33,41,42,43,44,45,46,47,48,49,50,52,56,57,58,59,60,61,63,64,65,77,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> IF PARENTESISIZQ expresion GT expresion PARENTESISDER LBRACE expresion SEMI RBRACE','declaracion',10,'p_declaracion_coditionif','Analizador Sintactico.py',30),
  ('declaracion -> ELSE LBRACE expresion SEMI RBRACE','declaracion',5,'p_declaracion_coditionelse','Analizador Sintactico.py',35),
  ('declaracion -> INT expresion ASIGNAR expresion SEMI','declaracion',5,'p_declaracion_asignar','Analizador Sintactico.py',40),
  ('declaracion -> DOUBLE expresion ASIGNAR expresion SEMI','declaracion',5,'p_declaracion_asignar2','Analizador Sintactico.py',44),
  ('declaracion -> INICIO','declaracion',1,'p_declaracion_taginicio','Analizador Sintactico.py',49),
  ('declaracion -> FIN','declaracion',1,'p_declaracion_tagfinal','Analizador Sintactico.py',54),
  ('declaracion -> expresion SEMI','declaracion',2,'p_declaracion_expr','Analizador Sintactico.py',59),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_operaciones','Analizador Sintactico.py',66),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_operaciones','Analizador Sintactico.py',67),
  ('expresion -> expresion MULTI expresion','expresion',3,'p_expresion_operaciones','Analizador Sintactico.py',68),
  ('expresion -> expresion DIVIDE expresion','expresion',3,'p_expresion_operaciones','Analizador Sintactico.py',69),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_minus','Analizador Sintactico.py',84),
  ('expresion -> PARENTESISIZQ expresion PARENTESISDER','expresion',3,'p_expresion_grupo','Analizador Sintactico.py',90),
  ('expresion -> LBRACE expresion RBRACE','expresion',3,'p_expresion_grupo','Analizador Sintactico.py',91),
  ('expresion -> expresion LT expresion','expresion',3,'p_expresion_logicas','Analizador Sintactico.py',99),
  ('expresion -> expresion GT expresion','expresion',3,'p_expresion_logicas','Analizador Sintactico.py',100),
  ('expresion -> expresion LE expresion','expresion',3,'p_expresion_logicas','Analizador Sintactico.py',101),
  ('expresion -> expresion GE expresion','expresion',3,'p_expresion_logicas','Analizador Sintactico.py',102),
  ('expresion -> expresion ASIGNAR expresion','expresion',3,'p_expresion_logicas','Analizador Sintactico.py',103),
  ('expresion -> expresion AS expresion','expresion',3,'p_expresion_logicas','Analizador Sintactico.py',104),
  ('expresion -> PARENTESISIZQ expresion LT expresion PARENTESISDER','expresion',5,'p_expresion_logicas','Analizador Sintactico.py',105),
  ('expresion -> PARENTESISIZQ expresion GT expresion PARENTESISDER','expresion',5,'p_expresion_logicas','Analizador Sintactico.py',106),
  ('expresion -> PARENTESISIZQ expresion LE expresion PARENTESISDER','expresion',5,'p_expresion_logicas','Analizador Sintactico.py',107),
  ('expresion -> PARENTESISIZQ expresion GE expresion PARENTESISDER','expresion',5,'p_expresion_logicas','Analizador Sintactico.py',108),
  ('expresion -> PARENTESISIZQ expresion ASIGNAR expresion PARENTESISDER','expresion',5,'p_expresion_logicas','Analizador Sintactico.py',109),
  ('expresion -> PARENTESISIZQ expresion AS expresion PARENTESISDER','expresion',5,'p_expresion_logicas','Analizador Sintactico.py',110),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','Analizador Sintactico.py',139),
  ('expresion -> NUMERO','expresion',1,'p_expresion_numero','Analizador Sintactico.py',143),
  ('expresion -> ID','expresion',1,'p_expresion_id','Analizador Sintactico.py',147),
]
