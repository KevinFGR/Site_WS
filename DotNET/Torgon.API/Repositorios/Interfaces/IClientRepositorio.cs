using Torgon.API.Models;

namespace Torgon.API.Repositorios.Interfaces
{
    public interface IClientRepositorio
    {
         Task<List<ClientModel>> GetAllClients();
         Task<ClientModel> GetClientById(int id);
         Task<ClientModel> AddClient(ClientModel model);
         Task<ClientModel> UpdateClient(ClientModel model, int id);
         Task<bool> DeleteClient(int id);
    }
}