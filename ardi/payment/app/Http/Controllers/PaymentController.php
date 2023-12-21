<?php

namespace App\Http\Controllers;

use App\Models\payment;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Xendit\Configuration;
use Xendit\Invoice\InvoiceApi;

class PaymentController extends Controller
{
    public function __construct()
    {
        Configuration::setXenditKey("xnd_development_pRASWGj9hhFZJi0cJCViKOp69Y1jg7DciEQVkXGSR9NbZ6l7qjDgV5r2qdG3");
        $this->apiInstance = new InvoiceApi();
    }

    public function store(Request $request)
    {
        $create_invoice_request = new Xendit\Invoice\CreateInvoiceRequest([
            'external_id' => (string) Str::uuid(),
            'description' => $request->description,
            'amount' => $request->amount,
            // 'invoice_duration' => $request->payer_email,
            'currency' => 'IDR',
            'reminder_time' => 1,
        ]);
        $result = $this->apiInstance->createInvoice($create_invoice_request);

        $payment = new payment();
        $payment->status = 'pending';
        $payment->checkout_link = $result['invoice_url'];
        $payment->external_id = $result['external_id'];
        $payment->save();

        return response()->json($payment);

    }
}
