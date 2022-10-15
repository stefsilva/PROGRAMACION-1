from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class VentasWindow(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def agregar_producto_codigo(self, codigo):
		print(" Se mando", codigo)

	def agregar_producto_nombre(self, nombre):
		print(" Se mando", nombre)

	def eliminar_producto(self):
		print("eliminar producto seleccionado")

	def modificar_producto(self):
		print("modificar producto seleccionado")

	def admin(self):
		print("Admin presionado")

	def sigout(self):
		print ("Sigout presionado")



class VentasApp(App):
	def build(self):
		return VentasWindow()

if __name__=="__main__":
	VentasApp().run()
