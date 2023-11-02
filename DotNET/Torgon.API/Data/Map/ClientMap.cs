using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Microsoft.EntityFrameworkCore.Metadata.Conventions;
using Torgon.API.Models;

namespace Torgon.API.Data.Map;

public class ClientMap : IEntityTypeConfiguration<ClientModel>
{
    public void Configure(EntityTypeBuilder<ClientModel> builder)
    {
        builder.HasKey(x=>x.Id);
        builder.Property(x=>x.Cpf).IsRequired().HasMaxLength(100);
        builder.Property(x=>x.Name).IsRequired().HasMaxLength(250);
        builder.Property(x=>x.Email).IsRequired().HasMaxLength(100);
        builder.Property(x=>x.Number).IsRequired();
        builder.Property(x=>x.Pass).IsRequired().HasMaxLength(250);
        builder.Property(x=>x.Address).IsRequired().HasMaxLength(1000);
    }
}