<select name="pageToggle" id="pageToggle" [(ngModel)]="pagesize" (change)="pageChangeForTable1(($event.target as HTMLSelectElement).value)">
  <!-- Options generation code -->
</select>
