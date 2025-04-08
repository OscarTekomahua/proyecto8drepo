import React, { useState } from "react";
import axios from "axios";

const EditUserModal = ({ user, onClose, onSuccess }) => {
  const [formData, setFormData] = useState({ ...user });

  const getAccessToken = () => localStorage.getItem("accessToken");
  const getRefreshToken = () => localStorage.getItem("refreshToken");

  const refreshAccessToken = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/users/token/refresh/", {
        refresh: getRefreshToken(),
      });
      localStorage.setItem("accessToken", res.data.access);
      return res.data.access;
    } catch (error) {
      console.error("Error al refrescar el token", error);
      alert("Tu sesión ha expirado.");
      window.location.href = "/login";
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSave = async () => {
    const confirm = window.confirm("¿Seguro que deseas actualizar al usuario?");
    if (!confirm) return;

    let token = getAccessToken();
    try {
      await axios.put(`http://127.0.0.1:8000/users/api/${user.id}/`, formData, {
        headers: { Authorization: `Bearer ${token}` },
      });
      alert("Usuario actualizado exitosamente");
      onClose();
      onSuccess();
    } catch (error) {
      if (error.response?.status === 401) {
        token = await refreshAccessToken();
        try {
          await axios.put(`http://127.0.0.1:8000/users/api/${user.id}/`, formData, {
            headers: { Authorization: `Bearer ${token}` },
          });
          alert("Usuario actualizado exitosamente");
          onClose();
          onSuccess();
        } catch (err) {
          alert("Error al actualizar después de refrescar token");
        }
      } else {
        console.error("Error al actualizar:", error);
        alert("Error al actualizar usuario");
      }
    }
  };

  return (
    <div className="modal d-block" tabIndex="-1" style={{ backgroundColor: "rgba(0,0,0,0.5)" }}>
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Editar Usuario</h5>
            <button type="button" className="btn-close" onClick={onClose}></button>
          </div>
          <div className="modal-body">
            <input
              name="name"
              className="form-control mb-2"
              placeholder="Nombre"
              value={formData.name}
              onChange={handleChange}
            />
            <input
              name="surname"
              className="form-control mb-2"
              placeholder="Apellido"
              value={formData.surname}
              onChange={handleChange}
            />
            <input
              name="control_number"
              className="form-control mb-2"
              placeholder="Matrícula"
              value={formData.control_number}
              onChange={handleChange}
            />
            <input
              name="age"
              className="form-control mb-2"
              placeholder="Edad"
              value={formData.age}
              onChange={handleChange}
            />
            <input
              name="email"
              className="form-control mb-2"
              placeholder="Email"
              value={formData.email}
              onChange={handleChange}
            />
            <input
              name="tel"
              className="form-control"
              placeholder="Teléfono"
              value={formData.tel}
              onChange={handleChange}
            />
          </div>
          <div className="modal-footer">
            <button className="btn btn-secondary" onClick={onClose}>
              Cancelar
            </button>
            <button className="btn btn-primary" onClick={handleSave}>
              Guardar Cambios
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EditUserModal;
