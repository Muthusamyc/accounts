pageChangeForTable1(value: any) {
  if (value !== null && value !== undefined) {
    this.pagesize = Number(value); // Convert to number if necessary
    // Other logic related to page change
  }
}


<select name="pageToggle" id="pageToggle" [(ngModel)]="pagesize" (change)="pageChangeForTable1($event.target?.value)">
  <!-- Options generation code -->
</select>
pagesize: number = 1; // Initialize with a default value
