using Microsoft.EntityFrameworkCore;
using Torgon.API.Data.Map;
using Torgon.API.Models;

namespace Torgon.API.Data;

public class TorgonDBContext : DbContext{
    public TorgonDBContext(DbContextOptions<TorgonDBContext> options) : base (options)
    {
        
    }
    public DbSet<ClientModel> Clients { get; set; }
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfiguration(new ClientMap());
        base.OnModelCreating(modelBuilder);
    }
}