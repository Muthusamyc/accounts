pageChangeForTable1(event: Event) {
  const targetValue = (event.target as HTMLSelectElement)?.value;
  if (targetValue !== null && targetValue !== undefined) {
    this.pagesize = Number(targetValue); 
    // Perform additional operations if needed
  }
}
