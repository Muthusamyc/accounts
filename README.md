pageChangeForTable1(event: Event) {
  const value = (event.target as HTMLSelectElement)?.value;
  if (value !== null && value !== undefined) {
    this.pagesize = Number(value); 
    // Perform additional operations if needed
  }
}



<select name="pageToggle" id="pageToggle" [(ngModel)]="pagesize" (change)="pageChangeForTable1($event)">
  <ng-container *ngFor="let item of createRangeForTable1(p?.getLastPage() ?? 0)">
    <option [value]="item.value">{{ item.label }}</option>
  </ng-container>
</select>
