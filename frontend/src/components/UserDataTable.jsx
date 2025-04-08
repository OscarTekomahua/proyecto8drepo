import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios"; // Si deseas obtener datos desde una API
import "bootstrap-icons/font/bootstrap-icons.css";
import EditUserModal from "./EditUserModal";

const API_URL = "http://127.0.0.1:8000";

const UserDataTable = () => {
  const [data, setData] = useState([]); // Datos para la tabla
  const [loading, setLoading] = useState(true); // Estado de carga
  const [selectedUser, setSelectedUser] = useState(null);
  const [showEditModal, setShowEditModal] = useState(false);
  const loggedInUserId = JSON.parse(localStorage.getItem("user"))?.id;

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
  
  const fetchData = async () => {
    setLoading(true);
    const token = getAccessToken();
    try {
      const res = await axios.get(`${API_URL}/users/api/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setData(res.data);
    } catch (error) {
      console.error("Error al cargar los datos:", error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleDelete = async (userId) => {
    if (userId === loggedInUserId) {
      alert("No puedes eliminar tu propio usuario.");
      return;
    }

    const confirmed = window.confirm("¿Estás seguro de que deseas eliminar este usuario?");
    if (!confirmed) return;

    const token = getAccessToken();
    try {
      await axios.delete(`${API_URL}/users/api/${userId}/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      alert("Usuario eliminado con éxito");
      fetchData();
    } catch (error) {
      if (error.response?.status === 401) {
        token = await refreshAccessToken();
        try {
          await axios.delete(`${API_URL}/users/api/${userId}/`, {
            headers: { Authorization: `Bearer ${token}` },
          });
          alert("Usuario eliminado con éxito");
          fetchData();
        } catch (err) {
          alert("Error al eliminar después de refrescar token");
        }
      } else {
        console.error("Error al actualizar: ", error);
        alert("Error al eliminar usuario");
      }
    }
  };

  const handleEdit = (user) => {
    setSelectedUser(user);
    setShowEditModal(true);
  };

  // Configuración de columnas
  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name, // Selector de datos
      sortable: true, // Habilitar ordenamiento
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button
            className="btn btn-warning me-4"
            onClick={() => handleEdit(row)}
          >
            <i className="bi bi-pencil"></i>
          </button>
          <button
            className="btn btn-danger me-4"
            onClick={() => handleDelete(row.id)}
          >
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  // Obtener datos desde una API (puedes cambiar esta parte)
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />
      { showEditModal && (
        <EditUserModal
          user={selectedUser}
          onClose={() => setShowEditModal(false)}
          onSuccess={fetchData}
        />
      )

      }
    </div>
  );
};

export default UserDataTable;
