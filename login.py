#====================================================
# SISTEMA DE LOGIN CON INTERFAZ GRAFICA
#====================================================

from pydoc import text
import tkinter as tk
from tkinter import messagebox 
# Usuarios registrados en el sistema
# Formato: 'nombre_usuario': 'contraseña'
usuarios={
    'admin': 'Admin2024!',
    'estudiante1': 'Seguridad1',
    'estudiante2': 'Python2024',
    'invitado': 'Invitado1!'
}
# Maximo de intentos permitidos antes de bloquear
MAX_INTENTOS = 3

# Contador de intentos (lista para poder modificarlo
# desde dentro de las funciones)
intentos = [0]

#Funcion que verifica si las credenciales son correctas
def verificar_credenciales():
    Usuario = entrada_usuario.get()
    Contraseña = entrada_contrasena.get()

    #Si ya se agotaron los intentos y la contraseña es son correctos
    if Usuario in usuarios and usuarios[Usuario] == Contraseña:
        ventana_login.withdraw()   #ocultar ventana de login
        abrir_sesion(Usuario)  #Abrir ventana de sesion
    else:
        intentos[0] += 1
        restantes = MAX_INTENTOS - intentos[0]
        if restantes > 0:
            etiqueta_error.config(
                text=f'Credenciales incorrectas. Intentos restantes: {restantes}'
            )
        else:
            etiqueta_error.config(
                text='ACCESO BLOQUEADO: demasiados intentos fallidos.'
            )
            boton_login.config(state='disabled')
            entrada_usuario.config(state='disabled')
            entrada_contrasena.config(state='disabled')
# Funcion que abre la ventana de sesion activa
def abrir_sesion (nombre_usuario):
    ventana_sesion = tk.Toplevel()
    ventana_sesion.title("Sesion Activa")
    ventana_sesion.geometry("400x300")
    ventana_sesion.configure(bg='#1e1e2e')
    ventana_sesion.resizable(False, False)

    #Mensaje de bienvenida
    tk.Label(ventana_sesion,
             text=f'Bienvenido/a, {nombre_usuario}!',
                font=('Arial', 16, 'bold'),
                bg='#1e1e2e', fg='#a6e3a1').pack(pady=30)
    tk.Label(ventana_sesion, text='Sesion iniciada correctamente.',
             font=('Arial', 11), bg='#1e1e2e', fg='#cdd6f4').pack()
    # Cuadro con datos del usuario
    frame_info = tk.Frame(ventana_sesion, bg='#313244', padx=20, pady=15)
    frame_info.pack(pady=20, padx=30, fill='x')
    tk.Label(frame_info, text=f'Usuario: {nombre_usuario}',
             font=('Arial', 10), bg='#313244', fg='#cdd6f4',
             anchor='w').pack(fill='x')
    tk.Label(frame_info, text='Rol: Usuario estandar',
             font=('Arial', 10), bg='#313244', fg='#cdd6f4',
             anchor='w').pack(fill='x')
    tk.Label(frame_info, text='Estado: Activo',
             font=('Arial', 10), bg='#313244', fg='#a6e3a1',
             anchor='w').pack(fill='x')
    # Funcion interna para cerrar sesion
    def cerrar_sesion():
        ventana_sesion.destroy()
        ventana_login.deiconify()
        entrada_usuario.delete(0, tk.END)
        entrada_contrasena.delete(0, tk.END)
        etiqueta_error.config(text='')
        intentos[0] = 0
        boton_login.config(state='normal')
        entrada_usuario.config(state='normal')
        entrada_contrasena.config(state='normal')
    # Boton de cerrar sesion
    tk.Button(ventana_sesion, text='Cerrar Sesion',
              command=cerrar_sesion,
              bg='#f38ba8', fg='white',
              font=('Arial', 11, 'bold'),
              padx=20, pady=8, bd=0,
              cursor='hand2').pack(pady=10)
 # ============================================
# CONSTRUCCION DE LA VENTANA PRINCIPAL
# ============================================
ventana_login = tk.Tk()
ventana_login.title('Sistema de Login - CIB-07')
ventana_login.geometry('420x480')
ventana_login.configure(bg='#1e1e2e')
ventana_login.resizable(False, False)
# Encabezado
frame_header = tk.Frame(ventana_login, bg='#313244', pady=20)
frame_header.pack(fill='x')
tk.Label(frame_header, text='SISTEMA DE LOGIN',
 font=('Arial', 18, 'bold'), bg='#313244', fg='#cba6f7').pack()
tk.Label(frame_header, text='CIB-07 Modulo 7 - Ciberseguridad',
 font=('Arial', 10), bg='#313244', fg='#6c7086').pack()
# Formulario
frame_form = tk.Frame(ventana_login, bg='#1e1e2e', padx=40, pady=30)
frame_form.pack(fill='both', expand=True)
tk.Label(frame_form, text='Nombre de usuario', font=('Arial', 11),
 bg='#1e1e2e', fg='#cdd6f4', anchor='w').pack(fill='x')
entrada_usuario = tk.Entry(frame_form, font=('Arial', 12), bg='#313244',
 fg='#cdd6f4', insertbackground='white', bd=0,
 highlightthickness=1, highlightcolor='#cba6f7',
 highlightbackground='#45475a')
entrada_usuario.pack(fill='x', ipady=8, pady=(4, 16))
tk.Label(frame_form, text='Contrasena', font=('Arial', 11),
 bg='#1e1e2e', fg='#cdd6f4', anchor='w').pack(fill='x')
entrada_contrasena = tk.Entry(frame_form, font=('Arial', 12),
bg='#313244',
 fg='#cdd6f4', insertbackground='white', bd=0, show='*',
 highlightthickness=1, highlightcolor='#cba6f7',
 highlightbackground='#45475a')
entrada_contrasena.pack(fill='x', ipady=8, pady=(4, 24))
boton_login = tk.Button(frame_form, text='Iniciar Sesion',
 command=verificar_credenciales, bg='#cba6f7', fg='#1e1e2e',
 font=('Arial', 12, 'bold'), padx=20, pady=10, bd=0,
 cursor='hand2')
boton_login.pack(fill='x')
etiqueta_error = tk.Label(frame_form, text='', font=('Arial', 10),
 bg='#1e1e2e', fg='#f38ba8', wraplength=320)
etiqueta_error.pack(pady=(16, 0))
# Pie con usuarios de prueba
frame_pie = tk.Frame(ventana_login, bg='#181825', pady=12)
frame_pie.pack(fill='x', side='bottom')
tk.Label(frame_pie,
 text='Usuarios de prueba: admin / Admin2024! | invitado / Invitado1!',
 font=('Arial', 8), bg='#181825', fg='#45475a').pack()
# Permitir iniciar sesion con la tecla Enter
ventana_login.bind('<Return>', lambda e: verificar_credenciales())
# Iniciar el programa
ventana_login.mainloop()
