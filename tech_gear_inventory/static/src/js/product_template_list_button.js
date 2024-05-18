/** @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
export class ProductListController extends ListController {
   setup() {
       super.setup();
   }

    OnTestClick() {
        this.actionService.doAction('tech_gear_inventory.action_product_template_xlsx_wizard');
    }
}
registry.category("views").add("button_in_tree", {
   ...listView,
   Controller: ProductListController,
   buttonTemplate: "button_product_list.ListView.Buttons",
});