class Animal():
  def _init_(self, pcodAnimal,pNombreAnimal):
    
    self.__nomAnimal=pNombreAnimal
    self.__codigoAnimal=pcodAnimal
   

  def setNombre(self, pNombreAnimal):
    self.__nomAnimal=pNombreDeLaAnimal

  def setCodigo(self, pcodAnimal):
    self.__codigoAnimal=pcodAnimal

class Producto():
  def _init_(self, pcodProducto,pNombreProducto):
    
    self.__nomProducto=pNombreProducto
    self.__codigoProducto=pcodProducto
   

  def setNombre(self, pNombreProducto):
    self.__nomProducto=pNombreDeProducto

  def setCodigo(self, pcodProducto):
    self.__codigoProducto=pcodProducto
       
class Usuario(persona):

  
  def _init_(self, pIdUsuario, pNombreUsuario, pApellidosUsuario):

    self.__codigoUsuario=pIdUsuario
    self.__nombre=pNombreUsuario
    self.__apellidos=pApellidosUsuario


  def setIdUsuario(self, pIdPersona):
    self.__IdPersona=pIdPersona

  def setNombrePersona(self, pNombrePersona):
    self.__nombrePersona=pNombrePersona

  def setApellidosPersona(self, pApellidosPersona):
    self.__apellidosPersona=pApellidosPersona

  
  def getIdPersona(self):
    return self.__IdPersona
  def getNombrePersona(self):
    return self.__nombrePersona
  
  def getApellidosPersona(self):
    return self.__apellidosPersona

class Veterinario(Persona):
  
  def _init_(self, pIdVeterinario, pNombreVeterinario, pApellidoVeterinario):
    super()._init_(pIdPersona, pNombrePersona, pApellidoPersona)              
    

class Cliente(Persona,Animal):
  def _init_(self, pidPersona, pNombre, pApellido,pcodAnimal,pNombreAnimal):

    Persona._init_(self, pCodigoPersona, pNombrePersona, pApellidoPersona)
    
    Animal._init_(self, pCodigoAnimal,pNombreAnimal)class Animal:
  def _init_(self, pIdAnimal,pNombreDeLaAnimal):
    
    self.__nomAnimal=pNombreDeLaAnimal
    self.__codigoAnimal=pcodAnimal
  
  def setNombre(self, pNombreDeLaAnimal):
    self.__nomAnimal=pNombreDeLaAnimal

  def setCodigo(self, pIdAnimal):
    self.__codigoAnimal=pIdAnimal
    
  def getNombre(self):
    return self.__nomAnimal
    
  def getCodigo(self):
    return self.__nomCodigo


class Persona():

  
  def _init_(self, pIdPersona, pNombre, pApellidos):

    self.__IdPersona=pIdPersona
    self.__nombre=pNombre
    self.__apellidos=pApellidos

  def setIdPersona(self, pCodigoPersona):
    self.__codigoPersona=pCodigoPersona

  def setNombre(self, pNombre):
    self.__nombre=pNombre

  def setApellidos(self, pApellidos):
    self.__apellidos=pApellidos


  def getIdPersona(self):
    return self.__IdPersona
  def getNombre(self):
    return self.__nombrePersona
  
  def getApellidos(self):
    return self.__apellidosPersona

 class Agenda(Persona,Animal):
  def _init_(self, pIdPersona, pNombrePersona, pApellidoPersona,pCodigoAnimal,pNombreAnimal):

    Persona._init_(self, pIdPersona, pNombrePersona, pApellidoPersona)
    
    Animal._init_(self, pIdAnimal,pNombreAnimal)
class Veterinario(Persona):
  
  def _init_(self, pIdPersona, pNombrePersona, pApellidoPersona):
    super()._init_(pIdPersona, pNombrePersona, pApellidoPersona) 

def setDarTiempoTurno(self):
    print(" asignando turno...")

def setAsignarPaciente(self):
    print(" asignando Paciente...")
  
           
class Animal:
  def _init_(self, pcodAnimal,pNombreAnimal):
    
    self.__nomAnimal=pNombreAnimal
    self.__codigoAnimal=pcodAnimal
  

  def setCodigo(self, pcodAnimal):
    self.__codigoAnimal=pcodAnimal 

