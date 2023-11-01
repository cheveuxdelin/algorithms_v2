<html lang="ts">
  {#if true}
    <p>hola</p>
  {:else}
    <p>adios</p>
    {#each [1, 2, 3] as cachi}
      <div>{cachi}</div>
    {/each}
  {/if}
</html>
